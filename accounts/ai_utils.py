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



import re
import requests


def generate_ai_questions(student):

    prompt = f"""
Generate EXACTLY 5 interview multiple choice questions.

Candidate Profile:
- Academic: {student.academic}
- Specialization: {student.specialization}
- Designation: {student.designation}
- Tech Stack: {student.tech_stack}
- Core Specialization: {student.core_spec_v1} {student.core_spec_v2}
- Technical Skills: {student.technical_v1} {student.technical_v2}
- Non Technical Skills: {student.non_tech_v1} {student.non_tech_v2}

STRICT RULES:
1. Generate EXACTLY 5 questions
2. Each question must contain:
   - Question
   - A option
   - B option
   - C option
   - D option
   - Correct Answer
3. No explanations
4. No markdown
5. No extra text

STRICT FORMAT:

Question: <question>
A. <option>
B. <option>
C. <option>
D. <option>
Answer: <letter>

Question: <question>
A. <option>
B. <option>
C. <option>
D. <option>
Answer: <letter>

Question: <question>
A. <option>
B. <option>
C. <option>
D. <option>
Answer: <letter>
"""

    try:

        print("🚀 Calling Ollama...")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 800
                }
            },
            timeout=500
        )

        print("✅ Response received")

        data = response.json()

        text = data.get("response", "")

        print("RAW RESPONSE:\n", text)

        # regex extraction
        pattern = r"(Question:.*?Answer:\s*[A-D])"

        matches = re.findall(
            pattern,
            text,
            re.DOTALL
        )

        questions = [
            q.strip()
            for q in matches
        ]

        print("PARSED QUESTIONS:", len(questions))

        # fallback if insufficient questions
        if len(questions) < 5:
            print("⚠️ Using fallback questions")
            return fallback_questions(student)

        return questions[:5]

    except Exception as e:

        print("❌ ERROR:", e)

        return fallback_questions(student)


def fallback_questions(student):

    return [

        """Question: What is a REST API?
A. A database
B. A web service architecture
C. A programming language
D. A browser
Answer: B""",

        """Question: What does Django ORM do?
A. Manages databases
B. Handles CSS
C. Creates UI
D. Runs JavaScript
Answer: A""",

        """Question: What is React used for?
A. Backend
B. Database
C. Frontend UI
D. Networking
Answer: C"""
    ]