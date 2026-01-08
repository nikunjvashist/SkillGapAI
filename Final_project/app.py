import streamlit as st
import plotly.graph_objects as go
import spacy
from collections import Counter

from core.file_loader import load_file
from core.text_cleaner import clean_text

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Skill Gap Analysis Dashboard",
    layout="wide"
)

st.title("Skill Gap Analysis Dashboard")

# ================= LOAD NLP =================
nlp = spacy.load("en_core_web_sm")

# ================= SKILL EXTRACTION =================
def extract_jd_skills(jd_text, top_n=6):
    doc = nlp(jd_text.lower())
    skills = []

    TECH_HINTS = {
        "embedded", "microcontroller", "arduino", "pid",
        "control", "sensor", "actuator", "automation",
        "testing", "iot", "linux", "system"
    }

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip()
        if 1 <= len(phrase.split()) <= 3:
            if any(h in phrase for h in TECH_HINTS):
                skills.append(phrase.title())

    ranked = Counter(skills)
    return [s for s, _ in ranked.most_common(top_n)]

# ================= SKILL SCORING (CORE FIX) =================
def compute_skill_scores(skills, resume_text, jd_text):
    resume_l = resume_text.lower()
    jd_l = jd_text.lower()

    resume_scores = []
    jd_scores = []
    upskill = []

    for skill in skills:
        s = skill.lower()

        # JD importance
        freq = jd_l.count(s)
        if freq >= 3:
            jd_score = 90
        elif freq == 2:
            jd_score = 80
        else:
            jd_score = 70

        # Resume logic (KEY FIX)
        if s in resume_l:
            resume_score = jd_score   # SAME HEIGHT
        else:
            resume_score = 30         # LOW → UPSKILL
            upskill.append(skill)

        resume_scores.append(resume_score)
        jd_scores.append(jd_score)

    return resume_scores, jd_scores, upskill

# ================= FILE UPLOAD =================
resume_file = st.file_uploader("Upload Resume", ["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description", ["pdf", "docx", "txt"])

# ================= LAYOUT =================
left_col, right_col = st.columns([2, 1])

# ================= ROLE VIEW (ALWAYS SHOW) =================
with right_col:
    st.subheader("Role View")

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=[80, 70, 75, 65, 60],
        theta=["Technical Skills", "Soft Skills", "Experience", "Education", "Certifications"],
        fill="toself",
        name="Current Profile"
    ))
    radar.add_trace(go.Scatterpolar(
        r=[90, 85, 80, 75, 70],
        theta=["Technical Skills", "Soft Skills", "Experience", "Education", "Certifications"],
        fill="toself",
        name="Job Requirements"
    ))
    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=280
    )
    st.plotly_chart(radar, use_container_width=True)

# ================= MAIN LOGIC =================
if resume_file and jd_file:
    resume_text = clean_text(load_file(resume_file))
    jd_text = clean_text(load_file(jd_file))

    skills = extract_jd_skills(jd_text)

    if not skills:
        st.error("No meaningful skills found in Job Description.")
        st.stop()

    resume_scores, jd_scores, upskill = compute_skill_scores(
        skills, resume_text, jd_text
    )

    matched = sum(1 for s in resume_scores if s >= 70)
    missing = len(skills) - matched
    overall_match = int(sum(resume_scores) / (len(resume_scores) * 100) * 100)

    # ================= SKILL MATCH OVERVIEW =================
    with left_col:
        st.subheader("Skill Match Overview")

        c1, c2, c3 = st.columns(3)
        c1.metric("Overall Match", f"{overall_match}%")
        c2.metric("Matched Skills", matched)
        c3.metric("Missing Skills", missing)

        # ----- BAR CHART -----
        fig = go.Figure()
        fig.add_bar(
            x=skills,
            y=resume_scores,
            name="Resume Skills",
            marker_color="#4A90E2"
        )
        fig.add_bar(
            x=skills,
            y=jd_scores,
            name="Job Requirements",
            marker_color="#7ED321"
        )
        fig.update_layout(
            barmode="group",
            yaxis=dict(title="Match Percentage", range=[0, 100]),
            height=320
        )
        st.plotly_chart(fig, use_container_width=True)

        # ----- CIRCULAR BADGES -----
        badge_cols = st.columns(4)
        for col, skill, score in zip(badge_cols, skills[:4], resume_scores[:4]):
            color = "🟢" if score >= 70 else "🔴"
            col.markdown(f"### {score}%")
            col.markdown(f"{color} **{skill}**")

        # ----- SKILL COMPARISON -----
        st.subheader("Skill Comparison")
        for skill, score in zip(skills, resume_scores):
            st.progress(score / 100, text=skill)

        # ----- UPSKILLING -----
        st.subheader("Upskilling Recommendations")
        if upskill:
            for skill in upskill:
                st.info(f"📘 Recommended to upskill: **{skill}**")
        else:
            st.success("✅ No upskilling required. Skills match perfectly!")
