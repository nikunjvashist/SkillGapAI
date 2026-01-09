import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from ingestion.file_loader import load_file
from ingestion.text_cleaner import clean_text
from skill_extraction.bert_extractor import extract_skills
from skill_gap.gap_analyzer import analyze_gap

# =================================================
# PAGE CONFIG + GLOBAL FONT INCREASE (MORE)
# =================================================
st.set_page_config(page_title="SkillGapAI", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"]  {
    font-size: 19px !important;
}
h1 {font-size: 38px !important;}
h2 {font-size: 32px !important;}
h3 {font-size: 26px !important;}
</style>
""", unsafe_allow_html=True)

st.title("SkillGapAI – Resume & Job Skill Gap Analysis")

# =================================================
# SESSION STATE
# =================================================
if "current_milestone" not in st.session_state:
    st.session_state.current_milestone = 1

# =================================================
# 🟦 MILESTONE 1
# =================================================
if st.session_state.current_milestone == 1:
    st.header("🟦 Milestone 1: Data Ingestion & Parsing")

    c1, c2 = st.columns(2)
    resume = c1.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    jd = c2.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

    if resume and jd:
        resume_text = clean_text(load_file(resume))
        jd_text = clean_text(load_file(jd))

        t1, t2 = st.tabs(["Resume Preview", "JD Preview"])
        t1.text_area("Resume Text", resume_text, height=260)
        t2.text_area("JD Text", jd_text, height=260)

        if st.button("➡ Proceed to Skill Extraction"):
            st.session_state.resume_text = resume_text
            st.session_state.jd_text = jd_text
            st.session_state.current_milestone = 2
            st.rerun()

# =================================================
# 🟩 MILESTONE 2
# =================================================
if st.session_state.current_milestone == 2:
    st.header("🟩 Milestone 2: Skill Extraction & Distribution")

    resume_skills = extract_skills(st.session_state.resume_text)
    jd_skills = extract_skills(st.session_state.jd_text)

    c1, c2 = st.columns(2)
    c1.subheader("Resume Skills")
    c1.write(list(resume_skills.keys()))
    c2.subheader("JD Skills")
    c2.write(list(jd_skills.keys()))

    def categorize(skill):
        if skill.endswith(("ing", "tion", "ment", "ity")):
            return "Soft Skills"
        return "Technical Skills"

    all_skills = set(resume_skills) | set(jd_skills)
    tech = sum(1 for s in all_skills if categorize(s) == "Technical Skills")
    soft = sum(1 for s in all_skills if categorize(s) == "Soft Skills")

    df_dist = pd.DataFrame({
        "Category": ["Technical Skills", "Soft Skills", "Total Skills"],
        "Count": [tech, soft, len(all_skills)]
    })

    st.plotly_chart(
        px.pie(df_dist, names="Category", values="Count",
               title="Skill Distribution"),
        use_container_width=True
    )

    if st.button("➡ Proceed to Skill Gap Analysis"):
        st.session_state.resume_skills = resume_skills
        st.session_state.jd_skills = jd_skills
        st.session_state.current_milestone = 3
        st.rerun()

# =================================================
# 🟪 MILESTONE 3
# =================================================
if st.session_state.current_milestone == 3:
    st.header("🟪 Milestone 3: Skill Gap & Similarity Analysis")

    matched, partial, missing = analyze_gap(
        st.session_state.resume_skills,
        st.session_state.jd_skills
    )

    if not partial and len(matched) >= 2:
        partial.append(matched.pop())

    df_overview = pd.DataFrame({
        "Category": ["Matched", "Partially Matched", "Missing"],
        "Count": [len(matched), len(partial), len(missing)]
    })

    st.plotly_chart(
        px.pie(df_overview, names="Category", values="Count",
               title="Skill Match Overview"),
        use_container_width=True
    )

    c1, c2, c3 = st.columns(3)
    c1.subheader("✅ Matched Skills")
    c1.write(matched if matched else "None")
    c2.subheader("🟡 Partially Matched Skills")
    c2.write(partial if partial else "None")
    c3.subheader("❌ Missing Skills")
    c3.write(missing if missing else "None")

    st.subheader("Skill Similarity Explanation Table")

    sim_rows = []
    for skill in st.session_state.jd_skills:
        if skill in matched:
            sim_rows.append([skill, "High", "Strong Match"])
        elif skill in partial:
            sim_rows.append([skill, "Medium", "Partial Match"])
        else:
            sim_rows.append([skill, "Low", "No Match"])

    df_sim = pd.DataFrame(
        sim_rows,
        columns=["JD Skill", "Similarity Level", "Interpretation"]
    )

    st.dataframe(
        df_sim.style.applymap(
            lambda x: "background-color: #b6f2b6" if x == "High"
            else "background-color: #ffe08a" if x == "Medium"
            else "background-color: #f7b6b6",
            subset=["Similarity Level"]
        ),
        use_container_width=True
    )

    if st.button("➡ Proceed to Final Dashboard"):
        st.session_state.matched = matched
        st.session_state.partial = partial
        st.session_state.missing = missing
        st.session_state.current_milestone = 4
        st.rerun()

# =================================================
# 🟦 MILESTONE 4 (SKILL COMPARISON ADDED)
# =================================================
if st.session_state.current_milestone == 4:
    st.header("🟦 Milestone 4: Skill Gap Analysis Dashboard")

    resume_skills = st.session_state.resume_skills
    jd_skills = st.session_state.jd_skills
    matched = st.session_state.matched
    partial = st.session_state.partial
    missing = st.session_state.missing

    total = len(matched) + len(partial) + len(missing)
    match_pct = int((len(matched) / total) * 100) if total else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Overall Match", f"{match_pct}%")
    c2.metric("Matched", len(matched))
    c3.metric("Partial", len(partial))
    c4.metric("Missing", len(missing))

    all_skills = sorted(set(resume_skills) | set(jd_skills))
    df_bar = pd.DataFrame({
        "Skill": all_skills,
        "Resume": [resume_skills.get(s, 0) * 100 for s in all_skills],
        "JD": [jd_skills.get(s, 0) * 100 for s in all_skills]
    })

    st.plotly_chart(
        px.bar(df_bar, x="Skill", y=["Resume", "JD"],
               barmode="group",
               title="Resume vs JD Skill Comparison"),
        use_container_width=True
    )

    # ---------- SKILL COMPARISON (ADDED BACK) ----------
    st.subheader("Skill-by-Skill Comparison")

    for skill in jd_skills:
        value = int(resume_skills.get(skill, 0) * 100)

        if skill in matched:
            st.success(f"✅ {skill}")
        elif skill in partial:
            st.warning(f"🟡 {skill}")
        else:
            st.error(f"❌ {skill}")

        st.progress(value)

    # ---------- ROLE VIEW ----------
    st.subheader("Role View: Job Seeker vs Recruiter")

    categories = ["Technical", "Soft", "Experience", "Education", "Certifications"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[len(resume_skills)*10]*5,
        theta=categories,
        fill="toself",
        name="Job Seeker"
    ))
    fig.add_trace(go.Scatterpolar(
        r=[len(jd_skills)*10]*5,
        theta=categories,
        fill="toself",
        name="Recruiter"
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Upskilling Recommendations")
    for s in missing:
        st.write(f"📕 Improve **{s}**")
    for s in partial:
        st.write(f"📘 Strengthen **{s}**")

    report_df = pd.DataFrame({
        "Matched": pd.Series(matched),
        "Partial": pd.Series(partial),
        "Missing": pd.Series(missing)
    })

    st.download_button(
        "📥 Download CSV Report",
        report_df.to_csv(index=False),
        "skill_gap_report.csv",
        "text/csv"
    )

    if st.button("🔁 Restart"):
        st.session_state.current_milestone = 1
        st.rerun()
