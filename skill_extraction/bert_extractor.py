import re

# MASTER SKILL VOCAB (small, clean, extendable)
SKILL_VOCAB = [
    "embedded systems",
    "c programming",
    "microcontrollers",
    "basic automation",
    "advanced automation",
    "automation",
    "sensors",
    "sensors and actuators",
    "actuators",
    "iot protocols",
    "iot",
    "pid control",
    "can communication",
    "documentation",
    "problem solving"
]

def extract_skills(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    found_skills = {}

    for skill in SKILL_VOCAB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills[skill] = 1   # presence-based (COUNT SAFE)

    return found_skills
