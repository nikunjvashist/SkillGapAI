import spacy

nlp = spacy.load("en_core_web_sm")

STOP_WORDS = {
    "experience", "responsibilities", "requirements", "knowledge",
    "skills", "ability", "role", "work", "familiarity",
    "qualification", "communication", "key responsibilities"
}

def extract_skills(text):
    doc = nlp(text)
    skills = []

    for chunk in doc.noun_chunks:
        phrase = chunk.text.lower().strip()

        if (
            1 <= len(phrase.split()) <= 3 and
            phrase not in STOP_WORDS and
            not phrase.isdigit()
        ):
            skills.append(phrase)

    # remove duplicates but keep order
    skills = list(dict.fromkeys(skills))

    # IMPORTANT: limit skills → UI stays clean
    return skills[:10]
