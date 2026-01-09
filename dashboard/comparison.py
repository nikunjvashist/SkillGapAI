import streamlit as st

def skill_comparison(resume_skills, jd_skills):
    st.subheader("Skill Comparison")

    for skill in jd_skills:
        res_val = resume_skills.get(skill, 0) * 100
        jd_val = jd_skills.get(skill, 0) * 100

        st.write(skill)
        st.progress(int(res_val))
