import streamlit as st

def render_skill_overview(metrics):
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Overall Match", f"{metrics['overall_match']}%")

    with col2:
        st.metric("Matched Skills", metrics["matched"])

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Partial Matches", metrics["partial"])
    with col4:
        st.metric("Missing Skills", metrics["missing"])
