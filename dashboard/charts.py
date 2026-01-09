import pandas as pd
import plotly.express as px
import streamlit as st

def resume_vs_jd_bar(resume_skills, jd_skills):
    skills = sorted(set(resume_skills) | set(jd_skills))

    data = pd.DataFrame({
        "Skill": skills,
        "Resume": [resume_skills.get(s, 0)*100 for s in skills],
        "JD": [jd_skills.get(s, 0)*100 for s in skills]
    })

    fig = px.bar(
        data, x="Skill", y=["Resume", "JD"],
        barmode="group",
        title="Resume Skills vs Job Requirements"
    )
    st.plotly_chart(fig, use_container_width=True)


def role_radar_view(resume_skills, jd_skills):
    categories = ["Technical Skills", "Soft Skills", "Experience", "Education", "Certifications"]

    # simple normalization
    resume_score = min(len(resume_skills)*10, 100)
    jd_score = min(len(jd_skills)*10, 100)

    radar_data = pd.DataFrame({
        "Category": categories,
        "Resume": [resume_score]*5,
        "JD": [jd_score]*5
    })

    fig = px.line_polar(
        radar_data,
        r="Resume",
        theta="Category",
        line_close=True,
        title="Role View: Job Seeker vs Recruiter"
    )
    st.plotly_chart(fig, use_container_width=True)
