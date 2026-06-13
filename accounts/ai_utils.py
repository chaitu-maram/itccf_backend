
import re
import requests

from .models import QuestionBank


# ─────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────

NEEDED_PER_SECTION = 4
REUSE_LIMIT        = 15

# Only these sections allow loose (cross-stack) fallback from the bank
ALLOW_LOOSE_FALLBACK_SECTIONS = {"Personal", "Professional"}


# ─────────────────────────────────────────────────────────────
# Context helpers
# ─────────────────────────────────────────────────────────────

def _norm(value):
    return (value or "").strip().lower()


def _experience_level(student):
    raw = _norm(student.experience_years)
    if not raw or raw == "fresher":
        return "fresher"
    try:
        years = int(raw.replace("+", ""))
    except ValueError:
        return "fresher"
    if years <= 2:
        return "junior"
    if years <= 5:
        return "mid"
    return "senior"


def _job_interests(student):
    raw = []
    for attr in [
        "core_spec_v1",   "core_spec_v2",
        "technical_v1",   "technical_v2",
        "non_tech_v1",    "non_tech_v2",
        "general_cat_v1", "general_cat_v2",
        "job_nature_v1",  "job_nature_v2",
    ]:
        val = _norm(getattr(student, attr, "") or "")
        if val:
            raw.append(val)
    return list(dict.fromkeys(raw))


def _build_student_context(student):
    return {
        "tech_stack":       (student.tech_stack     or "general IT").strip(),
        "designation":      (student.designation    or "Professional").strip(),
        "specialization":   (student.specialization or "general").strip(),
        "experience_level": _experience_level(student),
        "experience_years": (student.experience_years or "Fresher").strip(),
        "job_interests":    _job_interests(student),
        "company_name":     (student.company_name   or "").strip(),
    }


# ─────────────────────────────────────────────────────────────
# QuestionBank — fetch
# ─────────────────────────────────────────────────────────────

def _get_from_bank(section, ctx):
    """
    Fetch up to NEEDED_PER_SECTION questions for a section.

    Tier 0  exact: tech + designation + specialization   (all sections)
    Tier 1  same tech_stack only                         (all sections)
    Tier 2  job_interest match                           (all sections)
    Tier 3  designation match                            (Personal/Professional ONLY)
    Tier 4  experience_level match                       (Personal/Professional ONLY)

    Technical section HARD STOPS after Tier 1.
    If < NEEDED questions found for Technical via Tier 0+1, we return
    whatever we found — the caller will fill the gap from Ollama/fallback.
    This guarantees a Java student NEVER gets ECE/Python questions.
    """

    base = (
        QuestionBank.objects
        .filter(section=section)
        .filter(times_used__lt=REUSE_LIMIT)
    )

    collected = []
    used_ids  = set()

    def _pull(qs, needed):
        """Pull `needed` rows, excluding already-collected ids."""
        rows = list(
            qs.exclude(id__in=used_ids)
            .order_by("times_used", "?")[:needed]
        )
        collected.extend(rows)
        used_ids.update(r.id for r in rows)

    def remaining():
        return NEEDED_PER_SECTION - len(collected)

    # ── Tier 0: exact match ───────────────────────────────────
    _pull(
        base.filter(
            tech_stack__iexact=ctx["tech_stack"],
            designation__iexact=ctx["designation"],
            specialization__iexact=ctx["specialization"],
        ),
        remaining()
    )
    if remaining() <= 0:
        return collected

    # ── Tier 1: same tech_stack ───────────────────────────────
    _pull(
        base.filter(tech_stack__iexact=ctx["tech_stack"]),
        remaining()
    )
    if remaining() <= 0:
        return collected

    # ── HARD STOP for Technical section ──────────────────────
    # Never serve cross-stack questions for Technical.
    # Return what we have (may be < NEEDED — caller handles the gap).
    if section == "Technical":
        print(
            f"  🔒 Technical hard-stop: found {len(collected)}/{NEEDED_PER_SECTION} "
            f"for tech_stack='{ctx['tech_stack']}'"
        )
        return collected

    # ── Tier 2: job_interest match (Personal / Professional) ──
    for interest in ctx["job_interests"]:
        if remaining() <= 0:
            break
        _pull(
            base.filter(job_interest__iexact=interest),
            remaining()
        )
    if remaining() <= 0:
        return collected

    # ── Tier 3: designation match ─────────────────────────────
    _pull(
        base.filter(designation__iexact=ctx["designation"]),
        remaining()
    )
    if remaining() <= 0:
        return collected

    # ── Tier 4: experience_level match ───────────────────────
    _pull(
        base.filter(experience_level=ctx["experience_level"]),
        remaining()
    )

    return collected


# ─────────────────────────────────────────────────────────────
# QuestionBank — save
# ─────────────────────────────────────────────────────────────

def _save_to_bank(parsed_questions, ctx):
    primary_interest = ctx["job_interests"][0] if ctx["job_interests"] else None

    objs = [
        QuestionBank(
            tech_stack=ctx["tech_stack"],
            designation=ctx["designation"],
            specialization=ctx["specialization"],
            job_interest=primary_interest,
            experience_level=ctx["experience_level"],
            section=section,
            question=q_text,
        )
        for section, q_text in parsed_questions
    ]
    if objs:
        QuestionBank.objects.bulk_create(objs)
        print(f"💾 Saved {len(objs)} questions to bank")


# ─────────────────────────────────────────────────────────────
# Static fallback — always correct, fully personalised
# ─────────────────────────────────────────────────────────────

def _fallback_questions(ctx):
    """
    Returns exactly 12 personalised static questions (4 per section).
    Never fails. Used when bank + Ollama don't cover all 12.
    """
    tech      = ctx["tech_stack"]
    desig     = ctx["designation"]
    spec      = ctx["specialization"]
    exp       = ctx["experience_years"]
    interests = ctx["job_interests"]

    primary_interest = interests[0] if interests else desig
    exp_context = (
        f"with {exp} years of experience"
        if exp and _norm(exp) != "fresher"
        else "as a fresher"
    )

    personal = [
        (
            f"What motivates you to pursue a career in {primary_interest}?",
            "Salary only",
            "Passion and career growth",
            "Family pressure",
            "Random choice",
            "B",
        ),
        (
            "How do you handle pressure or tight deadlines at work?",
            "Panic and stop working",
            "Stay calm, prioritize, and communicate",
            "Blame colleagues",
            "Ignore the deadline",
            "B",
        ),
        (
            "How do you respond to constructive criticism from a manager?",
            "Argue back",
            "Ignore it completely",
            "Accept it and use it to improve",
            "Get upset and quit",
            "C",
        ),
        (
            f"Why did you choose {spec} as your area of specialization?",
            "No other option was available",
            "Genuine interest and career potential",
            "Only family pressure",
            "Random choice with no reason",
            "B",
        ),
    ]

    technical = [
        (
            f"What is the primary purpose of {tech} in modern development?",
            "To design marketing logos",
            "To build, manage, and scale applications",
            "To handle HR and payroll tasks",
            "To write formal emails",
            "B",
        ),
        (
            f"Which practice is most important when working with {tech}?",
            "Writing messy, undocumented code",
            "Following coding standards and maintaining documentation",
            "Skipping unit testing to save time",
            "Avoiding version control entirely",
            "B",
        ),
        (
            f"What is a key technical skill required for a {desig} role using {tech}?",
            "Avoiding all communication",
            "Problem solving combined with strong technical knowledge",
            "Working without any defined deadlines",
            "Ignoring project requirements",
            "B",
        ),
        (
            f"How should a {desig} approach debugging a critical issue in {tech}?",
            "Restart the system and hope it resolves",
            "Isolate the issue, reproduce it, then fix and verify",
            "Delete the problematic code immediately",
            "Assign blame to another team member",
            "B",
        ),
    ]

    professional = [
        (
            f"How do you prioritize multiple tasks as a {desig} {exp_context}?",
            "Work on tasks in random order",
            "Assess urgency and impact, then plan and execute",
            "Only do the easiest tasks first",
            "Ignore all tasks until forced",
            "B",
        ),
        (
            "What is the right approach when you realize you will miss a deadline?",
            "Hide it from the team until the last moment",
            "Inform stakeholders early and propose a revised plan",
            "Blame a colleague for the delay",
            "Pretend the deadline never existed",
            "B",
        ),
        (
            "How do you professionally handle a disagreement with a teammate?",
            "Stop communicating with them entirely",
            "Discuss the issue calmly and work toward a solution",
            "Escalate immediately without attempting resolution",
            "Complain to everyone else in the office",
            "B",
        ),
        (
            f"What does professional accountability mean for a {desig} {exp_context}?",
            "Doing the bare minimum to get by",
            "Owning your work, decisions, and their outcomes",
            "Avoiding any additional responsibility",
            "Taking long breaks and missing meetings",
            "B",
        ),
    ]

    def fmt(items, section):
        return [
            (
                f"Section: {section}\n"
                f"Question: {q}\n"
                f"A. {a}\nB. {b}\nC. {c}\nD. {d}\n"
                f"Answer: {ans}"
            )
            for q, a, b, c, d, ans in items
        ]

    return (
        fmt(personal,      "Personal")      # [0:4]
        + fmt(technical,   "Technical")     # [4:8]
        + fmt(professional,"Professional")  # [8:12]
    )


# ─────────────────────────────────────────────────────────────
# Ollama call
# ─────────────────────────────────────────────────────────────

def _call_ollama(ctx):
    tech      = ctx["tech_stack"]
    desig     = ctx["designation"]
    spec      = ctx["specialization"]
    exp       = ctx["experience_years"]
    exp_level = ctx["experience_level"]
    interests = ctx["job_interests"]

    interest_line = (
        f"  Job interests    : {', '.join(interests[:4])}\n"
        if interests else ""
    )
    exp_line = (
        f"  Experience       : {exp} years ({exp_level} level)\n"
        if exp and _norm(exp) != "fresher"
        else "  Experience       : Fresher\n"
    )

    prompt = (
        "Generate exactly 12 MCQ interview questions.\n"
        "Output ONLY the 12 blocks — no numbering, no markdown, no extra text.\n\n"
        "Candidate profile:\n"
        f"  Role/Designation : {desig}\n"
        f"  Tech stack       : {tech}\n"
        f"  Specialization   : {spec}\n"
        f"{exp_line}"
        f"{interest_line}"
        "\nDistribution (STRICT — do not change section names):\n"
        "  - 4 questions   Section: Personal     (attitude, motivation, self-awareness)\n"
        f"  - 4 questions   Section: Technical    "
        f"(MUST be specific to {tech} only — absolutely no other language or technology)\n"
        f"  - 4 questions   Section: Professional "
        f"(workplace scenarios for a {desig} at {exp_level} level)\n"
        "\nEach block MUST follow this EXACT format (repeat 12 times, nothing else):\n"
        "Section: <Personal|Technical|Professional>\n"
        "Question: <question text>\n"
        "A. <option>\n"
        "B. <option>\n"
        "C. <option>\n"
        "D. <option>\n"
        "Answer: <A|B|C|D>\n"
    )

    try:
        print(
            f"🚀 Ollama → tech={tech} | desig={desig} | "
            f"exp={exp} ({exp_level}) | interests={interests[:3]}"
        )

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature":    0.4,
                    "num_predict":    1800,
                    "top_k":          20,
                    "top_p":          0.85,
                    "repeat_penalty": 1.1,
                },
            },
            timeout=240,
        )

        print("✅ Ollama responded")
        text = response.json().get("response", "")
        print("RAW (first 800 chars):\n", text[:800])

        pattern = r"(Section:\s*(?:Personal|Technical|Professional).*?Answer:\s*[A-Da-d])"
        matches = [m.strip() for m in re.findall(pattern, text, re.DOTALL | re.IGNORECASE)]

        personal     = [q for q in matches if re.search(r"Section:\s*Personal",     q, re.IGNORECASE)]
        technical    = [q for q in matches if re.search(r"Section:\s*Technical",    q, re.IGNORECASE)]
        professional = [q for q in matches if re.search(r"Section:\s*Professional", q, re.IGNORECASE)]

        print(
            f"  Parsed → Personal:{len(personal)} "
            f"Technical:{len(technical)} "
            f"Professional:{len(professional)}"
        )
        return personal, technical, professional

    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return [], [], []


# ─────────────────────────────────────────────────────────────
# Public entry point
# ─────────────────────────────────────────────────────────────

def generate_ai_questions(student, force_refresh=False):
    """
    Hybrid strategy — always returns exactly 12 question strings (4 per section).

    Priority:
      1. QuestionBank  (instant, strict tech-stack matching)
      2. Ollama        (generated + saved to bank for next time)
      3. Static fallback (personalised, never fails)

    When Ollama times out or fails, the Technical section falls back to
    personalised static questions — never cross-stack bank questions.
    """
    ctx = _build_student_context(student)
    print(f"📋 Context → {ctx}")

    SECTIONS = ["Personal", "Technical", "Professional"]
    bank_results = {}

    # ── Step 1: QuestionBank ──────────────────────────────────
    if not force_refresh:
        for section in SECTIONS:
            bank_results[section] = _get_from_bank(section, ctx)
            print(
                f"  Bank [{section}]: "
                f"{len(bank_results[section])}/{NEEDED_PER_SECTION} found"
            )
    else:
        bank_results = {s: [] for s in SECTIONS}

    fully_covered = all(
        len(bank_results[s]) >= NEEDED_PER_SECTION for s in SECTIONS
    )

    if fully_covered:
        print("⚡ All 12 served from QuestionBank (instant)")
        result = []
        for section in SECTIONS:
            for qb in bank_results[section][:NEEDED_PER_SECTION]:
                qb.times_used += 1
                qb.save(update_fields=["times_used"])
                result.append(qb.question)
        return result

    # ── Step 2: Ollama for the gap ────────────────────────────
    ai_personal, ai_technical, ai_professional = _call_ollama(ctx)

    # Save everything Ollama returned (only if it actually returned something)
    to_save = (
          [("Personal",     q) for q in ai_personal]
        + [("Technical",    q) for q in ai_technical]
        + [("Professional", q) for q in ai_professional]
    )
    if to_save:
        _save_to_bank(to_save, ctx)

    # ── Step 3: Assemble final 12 ─────────────────────────────
    fb = _fallback_questions(ctx)

    def pick(section, ai_list, fb_slice):
        """
        Priority within each section:
          bank (strict-matched) → Ollama → static fallback

        IMPORTANT: bank_results for Technical only contains same-tech-stack
        questions (hard-stopped in _get_from_bank), so this is always safe.
        """
        bank_texts = []
        for qb in bank_results.get(section, [])[:NEEDED_PER_SECTION]:
            qb.times_used += 1
            qb.save(update_fields=["times_used"])
            bank_texts.append(qb.question)

        combined = bank_texts + ai_list + fb_slice

        # Deduplicate preserving order (first occurrence wins)
        seen, unique = set(), []
        for item in combined:
            key = _norm(item[:100])
            if key not in seen:
                seen.add(key)
                unique.append(item)

        selected = unique[:NEEDED_PER_SECTION]

        # Safety net: if still short (shouldn't happen), pad with fallback
        if len(selected) < NEEDED_PER_SECTION:
            extras = [
                q for q in fb_slice
                if _norm(q[:100]) not in seen
            ]
            selected.extend(extras[:NEEDED_PER_SECTION - len(selected)])

        print(
            f"  pick [{section}]: bank={len(bank_texts)} "
            f"ai={len(ai_list)} fb_used={max(0, NEEDED_PER_SECTION - len(bank_texts) - len(ai_list))} "
            f"→ final={len(selected)}"
        )
        return selected

    final = (
          pick("Personal",     ai_personal,     fb[0:4])
        + pick("Technical",    ai_technical,    fb[4:8])
        + pick("Professional", ai_professional, fb[8:12])
    )

    print(f"✅ Final questions assembled: {len(final)} (target 12)")
    return final