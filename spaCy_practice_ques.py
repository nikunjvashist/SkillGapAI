import spacy
from spacy.matcher import PhraseMatcher
import json
import re

# -------------------- LOAD MODEL --------------------
nlp = spacy.load("en_core_web_sm")

# -------------------- TECHNICAL & SOFT SKILL LISTS --------------------
technical_skills_list = [
    "Python", "SQL", "Machine Learning", "NLP", "Data Science"
]

soft_skills_list = [
    "communication", "teamwork", "leadership", "problem solving", "time management"
]

# -------------------- PHRASE MATCHER (CASE-INSENSITIVE) --------------------
tech_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

tech_patterns = [nlp(skill) for skill in technical_skills_list]
tech_matcher.add("TECH_SKILLS", tech_patterns)

# -------------------- FUNCTION: EXTRACT TECHNICAL SKILLS --------------------
def extract_technical_skills(text):
    doc = nlp(text)
    matches = tech_matcher(doc)

    skills = []
    for match_id, start, end in matches:
        skill = doc[start:end].text.lower()
        skills.append(skill)

    return list(set(skills))  # remove duplicates


# -------------------- FUNCTION: EXTRACT SOFT SKILLS --------------------
def extract_soft_skills(text):
    doc = nlp(text)
    found_skills = set()

    for token in doc:
        token_text = token.text.lower()
        if token_text in soft_skills_list:
            found_skills.add(token_text)

    return list(found_skills)


# -------------------- FUNCTION: COMBINED SKILL EXTRACTION --------------------
def extract_skills(text):
    return {
        "technical_skills": extract_technical_skills(text),
        "soft_skills": extract_soft_skills(text)
    }


# -------------------- 1–11: BASIC EXTRACTION & CLEANING --------------------
text1 = "I have experience in Python and SQL."
print("1–2.", extract_technical_skills(text1))

text2 = "Experience in Python, NLP, and Machine Learning with SQL."
print("6.", extract_technical_skills(text2))

text3 = "Python; SQL, Python and Machine Learning; SQL."
print("10–11.", extract_technical_skills(text3))


# -------------------- 12–13: MULTI-SENTENCE EXTRACTION --------------------
paragraph = """
I worked with Python and SQL.
My work also involved NLP and Machine Learning.
Strong communication and teamwork skills were required.
"""

combined_skills = extract_skills(paragraph)
print("13.", json.dumps(combined_skills, indent=2))


# -------------------- 14: MATCH SQL BUT NOT NoSQL --------------------
def extract_sql_only(text):
    doc = nlp(text)
    skills = []

    for token in doc:
        if token.text == "SQL":
            skills.append("sql")

    return list(set(skills))


text4 = "Experience with SQL and NoSQL databases."
print("14.", extract_sql_only(text4))


# -------------------- 15: RESUME vs JOB DESCRIPTION --------------------
resume_text = """
Experienced Python developer with Machine Learning knowledge.
Strong communication and problem solving skills.
"""

job_description_text = """
Looking for a candidate skilled in Python, SQL, and NLP.
Good teamwork and time management required.
"""

resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_description_text)

print("15. Resume Skills:")
print(json.dumps(resume_skills, indent=2))

print("15. Job Description Skills:")
print(json.dumps(job_skills, indent=2))
