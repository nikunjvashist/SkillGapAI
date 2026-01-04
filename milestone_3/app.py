# ===== WINDOWS PATH FIX (VERY IMPORTANT) =====
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

# ===== SKILL EXTRACTION (MILESTONE 2) =====
from skill_extraction.spacy_skill_extractor import extract_spacy_skills

# ===== MILESTONE 3 CORE LOGIC =====
from skill_matching.bert_similarity import compute_similarity
from skill_matching.skill_gap_analyzer import analyze_skill_gap
from analytics.match_metrics import calculate_metrics

# ===== UI COMPONENTS =====
from ui_components.similarity_matrix_ui import render_similarity_matrix
from ui_components.skill_chart_ui import render_skill_donut
from ui_components.missing_skills_ui import render_missing_skills


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Milestone 3 | Skill Gap Analysis",
    layout="wide"
)

# ================= HEADER =================
st.markdown("""
<div style="background:#6a3fc7;padding:18px;border-radius:10px;color:white;">
    <h2>Milestone 3: Skill Gap Analysis and Similarity Matching</h2>
    <p>
        Module: Skill Gap Analysis & Similarity Matching •
        BERT embeddings • Cosine similarity • Missing skill identification
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ================= INPUT SECTION =================
st.subheader("Skill Gap Analysis Interface")

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "Paste Resume Text",
        height=230,
        placeholder="Paste resume content here..."
    )

with col2:
    jd_text = st.text_area(
        "Paste Job Description Text",
        height=230,
        placeholder="Paste job description content here..."
    )

analyze_btn = st.button("Analyze Skill Gap")

# ================= PROCESS =================
if analyze_btn and resume_text.strip() and jd_text.strip():

    # -------- SKILL EXTRACTION --------
    resume_skills, _ = extract_spacy_skills(resume_text)
    jd_skills, _ = extract_spacy_skills(jd_text)

    if len(resume_skills) == 0 or len(jd_skills) == 0:
        st.error("No skills detected. Please check the input text.")
    else:
        # -------- SIMILARITY COMPUTATION --------
        similarity_matrix = compute_similarity(resume_skills, jd_skills)

        # -------- SKILL GAP ANALYSIS (REFERENCE LOGIC) --------
        matched, partial, missing, matrix_points = analyze_skill_gap(
            resume_skills,
            jd_skills,
            similarity_matrix
        )

        # -------- METRICS --------
        metrics = calculate_metrics(matched, partial, missing)

        st.markdown("---")

        # ================= DASHBOARD LAYOUT =================
        left, right = st.columns([2.2, 1])

        # -------- LEFT: SIMILARITY MATRIX --------
        with left:
            st.subheader("Similarity Matrix")
            render_similarity_matrix(matrix_points)

        # -------- RIGHT: OVERVIEW + DONUT --------
        with right:
            st.subheader("Skill Match Overview")

            c1, c2 = st.columns(2)
            with c1:
                st.metric("Overall Match", f"{metrics['overall_match']}%")
            with c2:
                st.metric("Matched Skills", metrics["matched"])

            c3, c4 = st.columns(2)
            with c3:
                st.metric("Partial Matches", metrics["partial"])
            with c4:
                st.metric("Missing Skills", metrics["missing"])

            st.markdown("<br>", unsafe_allow_html=True)
            render_skill_donut(
                metrics["matched"],
                metrics["partial"],
                metrics["missing"]
            )

        # ================= MISSING SKILLS =================
        st.markdown("---")
        render_missing_skills(missing)
