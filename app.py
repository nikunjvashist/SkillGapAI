import streamlit as st

# UI components
from ui_components.skill_chart_ui import render_skill_chart
from ui_components.skill_tags_ui import render_skill_tags

# -----------------------------
# Skill classification logic
# -----------------------------
def classify_skill(jd_skill, resume_text):
    jd = jd_skill.lower()
    resume = resume_text.lower()

    # ✅ Exact match
    if jd in resume:
        return "matched"

    # 🟠 Partial matches
    if jd == "advanced statistics" and "basic statistics" in resume:
        return "partial"

    if jd == "communication" and "communicat" in resume:
        return "partial"

    # ❌ Missing
    return "missing"


# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="Resume–JD Skill Matcher",
    layout="wide"
)

st.title("📄 Resume vs Job Description Skill Matching")
st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
col_input_1, col_input_2 = st.columns(2)

with col_input_1:
    resume_text = st.text_area(
        "Paste Resume Text",
        height=260,
        value="""Data Scientist with experience in Machine Learning, Python, SQL,
Data Visualization, and Basic Statistics.
Built ML models and communicated insights with teams."""
    )

with col_input_2:
    jd_text = st.text_area(
        "Paste Job Description Text",
        height=260,
        value="""We are hiring a Machine Learning Engineer.

Required Skills:
Machine Learning, Python, SQL, Data Visualization

Preferred Skills:
Advanced Statistics, NoSQL, Cloud

Soft Skills:
Strong communication and team leadership."""
    )

# -----------------------------
# JD Skill Dictionary (SINGLE SOURCE OF TRUTH)
# -----------------------------
JD_SKILLS = [
    "Machine Learning",
    "Python",
    "SQL",
    "Data Visualization",
    "Advanced Statistics",
    "NoSQL",
    "Cloud",
    "Communication",
    "Team Leadership"
]

# -----------------------------
# Skill Classification
# -----------------------------
matched, partial, missing = [], [], []

for skill in JD_SKILLS:
    status = classify_skill(skill, resume_text)

    if status == "matched":
        matched.append(skill)
    elif status == "partial":
        partial.append(skill)
    else:
        missing.append(skill)

matched_count = len(matched)
partial_count = len(partial)
missing_count = len(missing)

overall_match = round((matched_count / len(JD_SKILLS)) * 100)

# -----------------------------
# Results Section
# -----------------------------
st.markdown("---")

col_left, col_right = st.columns([2.2, 1])

# 🔹 Similarity Matrix
with col_left:
    render_skill_chart(
        jd_skills=JD_SKILLS,
        matched=matched,
        partial=partial,
        missing=missing
    )

# 🔹 Overview + Pie
with col_right:
    st.subheader("Skill Match Overview")

    st.metric("Overall Match", f"{overall_match}%")
    st.metric("Matched Skills", matched_count)
    st.metric("Partial Matches", partial_count)
    st.metric("Missing Skills", missing_count)

    import matplotlib.pyplot as plt

    pie_labels = ["Matched", "Partial", "Missing"]
    pie_values = [matched_count, partial_count, missing_count]
    pie_colors = ["green", "orange", "red"]

    fig, ax = plt.subplots()
    ax.pie(
        pie_values,
        labels=pie_labels,
        colors=pie_colors,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")

    st.pyplot(fig)

# -----------------------------
# Skill Tags Section
# -----------------------------
render_skill_tags(
    matched=matched,
    partial=partial,
    missing=missing
)
