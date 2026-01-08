from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(resume_skills, jd_skills):
    results = []

    for jd_skill in jd_skills:
        best_score = 0

        for r_skill in resume_skills:
            score = util.cos_sim(
                model.encode(jd_skill, convert_to_tensor=True),
                model.encode(r_skill, convert_to_tensor=True)
            ).item()

            best_score = max(best_score, score)

        results.append((jd_skill, int(best_score * 100)))

    matched = [x for x in results if x[1] >= 70]
    partial = [x for x in results if 40 <= x[1] < 70]
    missing = [x for x in results if x[1] < 40]

    return matched, partial, missing
