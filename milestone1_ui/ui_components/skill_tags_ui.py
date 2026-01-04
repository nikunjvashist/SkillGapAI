import streamlit as st

def show_skill_tags(title, skills):
    st.markdown(f"### {title}")

    for skill in skills:
        st.markdown(
            f"""
            <span style="
                background-color: #E6F4EA;
                color: #000000;              /* 🔥 FIX: force black text */
                padding: 6px 14px;
                border-radius: 16px;
                margin: 6px;
                display: inline-block;
                font-size: 14px;
                font-weight: 500;
            ">
                {skill}
            </span>
            """,
            unsafe_allow_html=True
        )
