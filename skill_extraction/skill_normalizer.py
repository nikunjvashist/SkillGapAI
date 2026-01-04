def classify_skill(jd_skill, resume_text):
    jd = jd_skill.lower()
    resume = resume_text.lower()

    # Exact match
    if jd in resume:
        return "matched"

    # Partial matches
    if jd == "advanced statistics" and "basic statistics" in resume:
        return "partial"

    if jd == "communication" and "communicat" in resume:
        return "partial"

    # Missing
    return "missing"
