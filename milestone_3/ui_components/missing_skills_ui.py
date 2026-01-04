import streamlit as st

def render_missing_skills(missing_skills):
    st.subheader("Missing Skills")
    for skill in missing_skills:
        st.warning(skill)
