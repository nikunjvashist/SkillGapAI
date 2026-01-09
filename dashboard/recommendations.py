RECOMMENDATION_MAP = {
    "aws": "Complete AWS Certified Solutions Architect course",
    "statistics": "Enroll in Advanced Statistics program",
    "project": "Consider PMP certification",
    "sql": "Practice SQL on real-world datasets",
    "python": "Build 2–3 real Python projects"
}

def get_recommendations(missing_skills):
    recs = []
    for skill in missing_skills:
        for key in RECOMMENDATION_MAP:
            if key in skill.lower():
                recs.append(RECOMMENDATION_MAP[key])
    return recs
