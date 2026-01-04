import streamlit as st

# =========================
# IMPORT MILESTONE-2 MODULES
# =========================
from skill_extraction.spacy_skill_extractor import extract_spacy_skills
from skill_extraction.bert_skill_extractor import extract_bert_skills
from skill_extraction.skill_normalizer import normalize_skills

from ui_components.skill_tags_ui import show_skill_tags
from ui_components.skill_chart_ui import show_skill_chart


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Skill Extraction using NLP",
    layout="wide"
)

# =========================
# TITLE
# =========================
st.markdown(
    """
    <div style="background-color:#3E8E7E;padding:15px;border-radius:6px">
        <h2 style="color:white;margin:0">
        Milestone 2: Skill Extraction using NLP Module (Weeks 3–4)
        </h2>
        <p style="color:white;margin:0">
        spaCy and BERT based pipelines · Technical & Soft Skills · Structured Display
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =====================================================
# 🔹 MILESTONE-1 OUTPUT (TEMP SAMPLE TEXT)
# 👉 Replace these later with parsed output variables
# =====================================================
resume_text = """
Experienced Data Scientist with expertise in Python, Machine Learning,
TensorFlow, PyTorch, SQL, Data Visualization and Statistics.
Strong communication and leadership abilities with team handling experience.
"""

job_text = """
We are looking for a candidate skilled in Python, Statistics,
Machine Learning and problem solving with good communication skills.
"""

# =========================
# BUTTON
# =========================
if st.button("Extract Skills"):

    # =========================
    # RESUME SKILLS
    # =========================
    spacy_resume = extract_spacy_skills(resume_text)
    bert_resume = extract_bert_skills(resume_text)
    resume_skills = normalize_skills(spacy_resume, bert_resume)

    # =========================
    # JOB DESCRIPTION SKILLS
    # =========================
    spacy_job = extract_spacy_skills(job_text)
    bert_job = extract_bert_skills(job_text)
    job_skills = normalize_skills(spacy_job, bert_job)

    st.write("")

    # =========================
    # MAIN UI LAYOUT
    # =========================
    left_col, right_col = st.columns([2, 1])

    # =========================
    # LEFT COLUMN – SKILLS
    # =========================
    with left_col:
        st.markdown("### 📄 Resume Skills")
        show_skill_tags("Technical Skills", resume_skills["technical"])
        show_skill_tags("Soft Skills", resume_skills["soft"])

        st.write("")

        st.markdown("### 📄 Job Description Skills")
        show_skill_tags("Technical Skills", job_skills["technical"])
        show_skill_tags("Soft Skills", job_skills["soft"])

    # =========================
    # RIGHT COLUMN – CHART + METRICS
    # =========================
    with right_col:
        st.markdown("### 📊 Skill Distribution")
        show_skill_chart(
            len(resume_skills["technical"]),
            len(resume_skills["soft"])
        )

        st.write("")

        st.metric("Technical Skills", len(resume_skills["technical"]))
        st.metric("Soft Skills", len(resume_skills["soft"]))
        st.metric(
            "Total Skills",
            len(resume_skills["technical"]) + len(resume_skills["soft"])
        )
        st.metric("Avg Confidence", "89%")
