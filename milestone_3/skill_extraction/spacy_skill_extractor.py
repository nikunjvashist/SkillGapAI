import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

TECH_SKILLS = [
    "python", "sql", "machine learning", "tensorflow",
    "pytorch", "data visualization", "statistics"
]

SOFT_SKILLS = [
    "communication", "leadership", "teamwork",
    "problem solving", "critical thinking"
]

def extract_spacy_skills(text):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

    matcher.add("TECH", [nlp(skill) for skill in TECH_SKILLS])
    matcher.add("SOFT", [nlp(skill) for skill in SOFT_SKILLS])

    doc = nlp(text)
    tech, soft = set(), set()

    for match_id, start, end in matcher(doc):
        label = nlp.vocab.strings[match_id]
        skill = doc[start:end].text
        if label == "TECH":
            tech.add(skill)
        else:
            soft.add(skill)

    return list(tech), list(soft)
