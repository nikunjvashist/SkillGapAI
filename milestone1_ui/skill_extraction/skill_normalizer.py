def normalize_skills(spacy_out, bert_out):
    tech = set()
    soft = set()

    for s in spacy_out[0] + bert_out[0]:
        tech.add(s.lower().title())

    for s in spacy_out[1] + bert_out[1]:
        soft.add(s.lower().title())

    return {
        "technical": list(tech)[:5],
        "soft": list(soft)[:5]
    }
