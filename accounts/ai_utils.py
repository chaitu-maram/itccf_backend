# import requests

# def generate_ai_questions(student):
#     prompt = f"""
# Generate exactly 4 multiple choice interview questions.

# Candidate Profile:
# - Academic: {student.academic}
# - Specialization: {student.specialization}
# - Designation: {student.designation}
# - Tech Stack: {student.tech_stack}
# - Core Specialization: {student.core_spec_v1} {student.core_spec_v2}
# - Technical Skills: {student.technical_v1} {student.technical_v2}
# - Non Technical Skills: {student.non_tech_v1} {student.non_tech_v2}

# Rules:
# - Only questions
# - One question per line
# - No explanations
# - No numbering (just plain questions)
# """

#     try:
#         print("🚀 Calling Ollama...")

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "phi3",   # 🔥 faster than llama3
#                 "prompt": prompt,
#                 "stream": False,
#                 "options": {
#                     "num_predict": 200
#                 }
#             },
#             timeout=120
#         )

#         print("✅ Response received")

#         data = response.json()
#         text = data.get("response", "")

#         print("RAW RESPONSE:\n", text)

#         questions = []

#         for line in text.split("\n"):
#             line = line.strip()

#             if line:
#                 cleaned = line.lstrip("0123456789.)- ").strip()

#                 if cleaned:
#                     questions.append(cleaned)

#         # fallback if AI fails
#         if not questions:
#             return fallback_questions(student)

#         return questions[:4]

#     except Exception as e:
#         print("❌ ERROR:", e)
#         return fallback_questions(student)


# def fallback_questions(student):
#     questions = []

#     if student.tech_stack:
#         questions.append(f"Explain your experience with {student.tech_stack}")

#     if student.specialization:
#         questions.append(f"What are key concepts in {student.specialization}?")

#     if student.designation:
#         questions.append(f"What is your role as {student.designation}?")

#     while len(questions) < 4:
#         questions.append("Tell me about a challenge you solved.")

#     return questions



# import requests


# def generate_ai_questions(student):
#     prompt = f"""
# Generate exactly 3 multiple choice interview questions.

# Candidate Profile:
# - Academic: {student.academic}
# - Specialization: {student.specialization}
# - Designation: {student.designation}
# - Tech Stack: {student.tech_stack}
# - Core Specialization: {student.core_spec_v1} {student.core_spec_v2}
# - Technical Skills: {student.technical_v1} {student.technical_v2}
# - Non Technical Skills: {student.non_tech_v1} {student.non_tech_v2}

# Rules:
# - Each question must have 4 options (A, B, C, D)
# - Only ONE correct answer
# - Clearly mention the correct answer
# - Format STRICTLY like this:

# Question: <question text>
# A. option
# B. option
# C. option
# D. option
# Answer: <correct option letter>

# - Separate each question with a blank line
# - Do NOT add explanations
# """

#     try:
#         print("🚀 Calling Ollama...")

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "phi3",   # fast model
#                 "prompt": prompt,
#                 "stream": False,
#                 "options": {
#                     "num_predict": 300
#                 }
#             },
#             timeout=120
#         )

#         print("✅ Response received")

#         data = response.json()
#         text = data.get("response", "")

#         print("RAW RESPONSE:\n", text)

#         # ✅ split into full MCQ blocks
#         blocks = text.split("\n\n")

#         questions = []
#         for block in blocks:
#             block = block.strip()
#             if block:
#                 questions.append(block)

#         # fallback if AI fails
#         if not questions:
#             return fallback_questions(student)

#         return questions[:3]

#     except Exception as e:
#         print("❌ ERROR:", e)
#         return fallback_questions(student)


# # ✅ fallback in MCQ format
# def fallback_questions(student):
#     return [
#         """Question: What is a REST API?
# A. A database
# B. A web service architecture
# C. A programming language
# D. A browser
# Answer: B""",

#         """Question: What does Django ORM do?
# A. Manages databases
# B. Handles CSS
# C. Creates UI
# D. Runs JavaScript
# Answer: A""",

#         """Question: What is React used for?
# A. Backend
# B. Database
# C. Frontend UI
# D. Networking
# Answer: C""",

#         """Question: What is Git?
# A. Operating system
# B. Version control system
# C. Database
# D. IDE
# Answer: B"""
#     ]



# import re
# import requests


# def generate_ai_questions(student):

#     prompt = f"""
# Generate EXACTLY 5 low level interview multiple choice questions.

# Candidate Profile:
# - Academic: {student.academic}
# - Specialization: {student.specialization}
# - Designation: {student.designation}
# - Tech Stack: {student.tech_stack}
# - Core Specialization: {student.core_spec_v1} {student.core_spec_v2}
# - Technical Skills: {student.technical_v1} {student.technical_v2}
# - Non Technical Skills: {student.non_tech_v1} {student.non_tech_v2}

# STRICT RULES:
# 1. Generate EXACTLY 5 questions
# 2. Each question must contain:
#    - Question
#    - A option
#    - B option
#    - C option
#    - D option
#    - Correct Answer
# 3. No explanations
# 4. No markdown
# 5. No extra text

# STRICT FORMAT:

# Question: <question>
# A. <option>
# B. <option>
# C. <option>
# D. <option>
# Answer: <letter>

# Question: <question>
# A. <option>
# B. <option>
# C. <option>
# D. <option>
# Answer: <letter>

# Question: <question>
# A. <option>
# B. <option>
# C. <option>
# D. <option>
# Answer: <letter>
# """

#     try:

#         print("🚀 Calling Ollama...")

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "phi3",
#                 "prompt": prompt,
#                 "stream": False,
#                 "options": {
#                     "temperature": 0.3,
#                     "num_predict": 800
#                 }
#             },
#             timeout=300
#         )

#         print("✅ Response received")

#         data = response.json()

#         text = data.get("response", "")

#         print("RAW RESPONSE:\n", text)

#         # regex extraction
#         pattern = r"(Question:.*?Answer:\s*[A-D])"

#         matches = re.findall(
#             pattern,
#             text,
#             re.DOTALL
#         )

#         questions = [
#             q.strip()
#             for q in matches
#         ]

#         print("PARSED QUESTIONS:", len(questions))

#         # fallback if insufficient questions
#         if len(questions) < 5:
#             print("⚠️ Using fallback questions")
#             return fallback_questions(student)

#         return questions[:5]

#     except Exception as e:

#         print("❌ ERROR:", e)

#         return fallback_questions(student)


# def fallback_questions(student):

#     return [

#         """Question: What is a REST API?
# A. A database
# B. A web service architecture
# C. A programming language
# D. A browser
# Answer: B""",

#         """Question: What does Django ORM do?
# A. Manages databases
# B. Handles CSS
# C. Creates UI
# D. Runs JavaScript
# Answer: A""",

#         """Question: What is React used for?
# A. Backend
# B. Database
# C. Frontend UI
# D. Networking
# Answer: C"""
#     ]


# import re
# import requests


# def fallback_questions(student):
#     tech  = student.tech_stack     or "software development"
#     desig = student.designation    or "professional"
#     spec  = student.specialization or "your field"

#     personal = [
#         ("What motivates you to work hard every day?",
#          "Money only", "Growth and learning", "Avoiding work", "Peer pressure", "B"),
#         ("How do you handle pressure at work?",
#          "Panic and stop working", "Stay calm and prioritize tasks", "Blame others", "Ignore it", "B"),
#         ("How do you respond to constructive criticism?",
#          "Argue back", "Ignore it", "Accept and improve", "Get upset", "C"),
#         (f"Why did you choose {spec} as your field?",
#          "No other option", "Passion and career growth", "Family pressure only", "Random choice", "B"),
#     ]

#     technical = [
#         (f"What is the main purpose of {tech}?",
#          "To design logos", "To build and manage applications", "To handle HR tasks", "To write emails", "B"),
#         (f"Which practice is most important when working with {tech}?",
#          "Writing messy code", "Following coding standards and documentation", "Skipping testing", "Avoiding version control", "B"),
#         ("What does debugging mean in software development?",
#          "Writing new code", "Finding and fixing errors in code", "Deploying to production", "Designing the UI", "B"),
#         (f"What is a key skill needed for a {desig} role?",
#          "Avoiding communication", "Problem solving and technical knowledge", "Working without deadlines", "Ignoring requirements", "B"),
#     ]

#     professional = [
#         (f"How do you prioritize tasks as a {desig}?",
#          "Work randomly", "Assess urgency and importance then plan", "Do easiest tasks first", "Ignore all tasks", "B"),
#         ("What do you do when you miss a deadline?",
#          "Hide it from the team", "Inform the team early and recover the plan", "Blame a colleague", "Pretend it did not happen", "B"),
#         ("How do you handle a disagreement with a colleague?",
#          "Stop talking to them", "Discuss calmly and find a solution", "Escalate immediately", "Complain to everyone", "B"),
#         ("What does professional responsibility mean to you?",
#          "Doing only minimum work", "Owning your work and its outcomes", "Avoiding extra tasks", "Taking long breaks", "B"),
#     ]

#     result = []
#     for q, a, b, c, d, ans in personal:
#         result.append(f"Section: Personal\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
#     for q, a, b, c, d, ans in technical:
#         result.append(f"Section: Technical\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
#     for q, a, b, c, d, ans in professional:
#         result.append(f"Section: Professional\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
#     return result


# def generate_ai_questions(student):

#     full_name        = f"{student.surname or ''} {student.name or ''}".strip() or "Candidate"
#     experience       = f"{student.experience_years or '0'} years {student.experience_months or '0'} months"
#     core_specs       = " / ".join(filter(None, [student.core_spec_v1, student.core_spec_v2]))
#     technical_skills = " / ".join(filter(None, [student.technical_v1, student.technical_v2]))
#     non_tech_skills  = " / ".join(filter(None, [student.non_tech_v1, student.non_tech_v2]))
#     general_cat      = " / ".join(filter(None, [student.general_cat_v1, student.general_cat_v2]))
#     job_nature       = " / ".join(filter(None, [student.job_nature_v1, student.job_nature_v2]))

#     prompt = f"""You are an HR interview assistant. Generate exactly 6 multiple choice questions for the following candidate.

# === CANDIDATE PROFILE ===
# Name              : {full_name}
# Academic          : {student.academic or 'Not specified'}
# Specialization    : {student.specialization or 'Not specified'}
# Experience        : {experience}
# Designation       : {student.designation or 'Not specified'}
# Tech Stack        : {student.tech_stack or 'Not specified'}
# Technical Skills  : {technical_skills or 'Not specified'}
# Core Specialization : {core_specs or 'Not specified'}
# Job Nature          : {job_nature or 'Not specified'}
# =========================

# SECTION RULES:
# - Section Personal  (2 Qs): Basic attitude and motivation questions for this candidate.
# - Section Technical (2 Qs): Basic questions about {student.tech_stack or 'general IT'} and {technical_skills or 'technical skills'}.
# - Section Professional (2 Qs): Basic workplace and responsibility questions for a {student.designation or 'professional'}.

# OUTPUT FORMAT — repeat exactly 6 times:

# Section: Personal
# Question: [question]
# A. [option]
# B. [option]
# C. [option]
# D. [option]
# Answer: [A or B or C or D]

# STRICT RULES:
# 1. Output ONLY the 6 question blocks — nothing else
# 2. No numbering, no markdown, no headers, no explanations
# 3. Answer must be a single letter: A, B, C, or D"""

#     try:
#         print("🚀 Calling Ollama...")

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "phi3",
#                 "prompt": prompt,
#                 "stream": False,
#                 "options": {
#                     "temperature": 0.4,
#                     "num_predict": 1800,
#                     "stop": []
#                 }
#             },
#             timeout=300
#         )

#         print("✅ Response received")

#         data = response.json()
#         text = data.get("response", "")

#         print("RAW RESPONSE:\n", text)

#         pattern   = r"(Section:\s*(?:Personal|Technical|Professional).*?Answer:\s*[A-Da-d])"
#         matches   = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
#         questions = [q.strip() for q in matches]

#         print(f"PARSED QUESTIONS: {len(questions)}")

#         personal     = [q for q in questions if re.search(r"Section:\s*Personal",     q, re.IGNORECASE)]
#         technical    = [q for q in questions if re.search(r"Section:\s*Technical",    q, re.IGNORECASE)]
#         professional = [q for q in questions if re.search(r"Section:\s*Professional", q, re.IGNORECASE)]

#         print(f"  Personal: {len(personal)}, Technical: {len(technical)}, Professional: {len(professional)}")

#         fb    = fallback_questions(student)
#         final = (personal + fb[0:2])[:2] + (technical + fb[2:4])[:2] + (professional + fb[4:6])[:2]

#         print(f"FINAL QUESTIONS: {len(final)}")
#         return final

#     except Exception as e:
#         print(f"❌ ERROR: {e}")
#         return fallback_questions(student)



import re
import requests


def fallback_questions(student):
    tech  = student.tech_stack     or "software development"
    desig = student.designation    or "professional"
    spec  = student.specialization or "your field"

    personal = [
        ("What motivates you to work hard every day?",
         "Money only", "Growth and learning", "Avoiding work", "Peer pressure", "B"),
        ("How do you handle pressure at work?",
         "Panic and stop working", "Stay calm and prioritize tasks", "Blame others", "Ignore it", "B"),
        ("How do you respond to constructive criticism?",
         "Argue back", "Ignore it", "Accept and improve", "Get upset", "C"),
        (f"Why did you choose {spec} as your field?",
         "No other option", "Passion and career growth", "Family pressure only", "Random choice", "B"),
    ]

    technical = [
        (f"What is the main purpose of {tech}?",
         "To design logos", "To build and manage applications", "To handle HR tasks", "To write emails", "B"),
        (f"Which practice is most important when working with {tech}?",
         "Writing messy code", "Following coding standards and documentation", "Skipping testing", "Avoiding version control", "B"),
        ("What does debugging mean in software development?",
         "Writing new code", "Finding and fixing errors in code", "Deploying to production", "Designing the UI", "B"),
        (f"What is a key skill needed for a {desig} role?",
         "Avoiding communication", "Problem solving and technical knowledge", "Working without deadlines", "Ignoring requirements", "B"),
    ]

    professional = [
        (f"How do you prioritize tasks as a {desig}?",
         "Work randomly", "Assess urgency and importance then plan", "Do easiest tasks first", "Ignore all tasks", "B"),
        ("What do you do when you miss a deadline?",
         "Hide it from the team", "Inform the team early and recover the plan", "Blame a colleague", "Pretend it did not happen", "B"),
        ("How do you handle a disagreement with a colleague?",
         "Stop talking to them", "Discuss calmly and find a solution", "Escalate immediately", "Complain to everyone", "B"),
        ("What does professional responsibility mean to you?",
         "Doing only minimum work", "Owning your work and its outcomes", "Avoiding extra tasks", "Taking long breaks", "B"),
    ]

    result = []
    for q, a, b, c, d, ans in personal:
        result.append(f"Section: Personal\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
    for q, a, b, c, d, ans in technical:
        result.append(f"Section: Technical\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
    for q, a, b, c, d, ans in professional:
        result.append(f"Section: Professional\nQuestion: {q}\nA. {a}\nB. {b}\nC. {c}\nD. {d}\nAnswer: {ans}")
    return result


def generate_ai_questions(student):

    # ── Build only the fields actually used in the prompt ──────────────────
    desig = (student.designation    or "Professional").strip()
    tech  = (student.tech_stack     or "general IT").strip()
    spec  = (student.specialization or "general").strip()

    # Compact prompt — fewer tokens = faster generation on small models like phi3
    prompt = (
        "Generate exactly 6 MCQ interview questions. "
        "Output ONLY the 6 blocks below, nothing else, no numbering, no markdown.\n\n"
        f"Candidate: {desig}, {tech}, {spec}\n\n"
        "Rules:\n"
        "- 2 questions: Section Personal  (attitude/motivation)\n"
        f"- 2 questions: Section Technical (about {tech})\n"
        f"- 2 questions: Section Professional (workplace, {desig} role)\n\n"
        "Format (repeat exactly 6 times):\n"
        "Section: <Personal|Technical|Professional>\n"
        "Question: <text>\n"
        "A. <option>\n"
        "B. <option>\n"
        "C. <option>\n"
        "D. <option>\n"
        "Answer: <A|B|C|D>\n"
    )

    try:
        print("🚀 Calling Ollama...")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,   # lower = faster + more deterministic
                    "num_predict": 900,   # 6 questions need ~150 tokens each = 900 max
                    "top_k": 20,          # restrict sampling pool → faster inference
                    "top_p": 0.85,        # tighter nucleus sampling → faster
                    "repeat_penalty": 1.1,# discourages repetition without extra compute
                    "stop": [],
                },
            },
            timeout=180,  # reduced from 300 — phi3 should finish well within 3 min
        )

        print("✅ Response received")

        data = response.json()
        text = data.get("response", "")

        print("RAW RESPONSE:\n", text)

        pattern = r"(Section:\s*(?:Personal|Technical|Professional).*?Answer:\s*[A-Da-d])"
        matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
        questions = [q.strip() for q in matches]

        print(f"PARSED QUESTIONS: {len(questions)}")

        personal     = [q for q in questions if re.search(r"Section:\s*Personal",     q, re.IGNORECASE)]
        technical    = [q for q in questions if re.search(r"Section:\s*Technical",    q, re.IGNORECASE)]
        professional = [q for q in questions if re.search(r"Section:\s*Professional", q, re.IGNORECASE)]

        print(f"  Personal: {len(personal)}, Technical: {len(technical)}, Professional: {len(professional)}")

        fb    = fallback_questions(student)

        # Fill any missing sections from fallback so we always return exactly 6
        final = (personal     + fb[0:2])[:2] + \
                (technical    + fb[2:4])[:2] + \
                (professional + fb[4:6])[:2]

        print(f"FINAL QUESTIONS: {len(final)}")
        return final

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return fallback_questions(student)