from skill_matching.skill_mapper import map_skill_to_group

def analyze_skill_gap(resume_skills, jd_skills, similarity_matrix):
    matched = []
    partial = []
    missing = []
    matrix_points = []

    for j, jd_skill in enumerate(jd_skills):
        jd_group = map_skill_to_group(jd_skill)

        if not jd_group:
            missing.append(jd_skill)
            continue

        scores = similarity_matrix[:, j]
        max_score = scores.max().item()
        best_i = scores.argmax().item()
        resume_group = map_skill_to_group(resume_skills[best_i])

        # STRICTER LOGIC (KEY FIX)
        if resume_group == jd_group and max_score >= 0.85:
            status = "high"
            matched.append(jd_skill)

        elif max_score >= 0.60:
            status = "partial"
            partial.append(jd_skill)

        else:
            status = "low"
            missing.append(jd_skill)

        if resume_group:
            matrix_points.append({
                "x": jd_group,
                "y": resume_group,
                "status": status,
                "score": round(max_score, 2)
            })

    return matched, partial, missing, matrix_points
