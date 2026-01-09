def analyze_gap(resume_skills, jd_skills):
    resume_set = set(resume_skills.keys())
    jd_set = set(jd_skills.keys())

    matched = []
    partial = []
    missing = []

    for jd_skill in jd_set:
        if jd_skill in resume_set:
            matched.append(jd_skill)
        else:
            # check partial match (token overlap)
            jd_tokens = set(jd_skill.split())
            found_partial = False

            for res_skill in resume_set:
                res_tokens = set(res_skill.split())
                if len(jd_tokens & res_tokens) > 0:
                    partial.append(jd_skill)
                    found_partial = True
                    break

            if not found_partial:
                missing.append(jd_skill)

    return matched, partial, missing
