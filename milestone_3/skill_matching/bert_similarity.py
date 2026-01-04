from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(resume_skills, jd_skills):
    resume_embeddings = model.encode(resume_skills, convert_to_tensor=True)
    jd_embeddings = model.encode(jd_skills, convert_to_tensor=True)

    similarity_matrix = util.cos_sim(resume_embeddings, jd_embeddings)
    return similarity_matrix
