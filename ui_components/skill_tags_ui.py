import streamlit as st


def render_skill_tags(matched, partial, missing):
    st.markdown("---")

    # ✅ Matched Skills
    st.subheader("✅ Matched Skills")
    if matched:
        for skill in matched:
            st.success(skill)
    else:
        st.info("No matched skills found")

    # 🟠 Partial Matches
    st.subheader("🟠 Partial Matches")
    if partial:
        for skill in partial:
            st.warning(skill)
    else:
        st.info("No partial matches found")

    # ❌ Missing Skills
    st.subheader("❌ Missing Skills")
    if missing:
        for skill in missing:
            st.error(skill)
    else:
        st.success("No missing skills 🎉")
