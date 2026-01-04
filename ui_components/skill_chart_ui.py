import matplotlib.pyplot as plt
import streamlit as st


def render_skill_chart(jd_skills, matched, partial, missing):
    st.subheader("Similarity Matrix")

    fig, ax = plt.subplots(figsize=(9, 5))

    # Y-axis labels (resume side)
    resume_labels = [
        "ML",
        "Python",
        "SQL",
        "Data Visualization",
        "Stats (Basic)",
        "NoSQL",
        "Cloud",
        "Communication",
        "Team Leadership"
    ]

    # Plot matched (green)
    for i, skill in enumerate(jd_skills):
        if skill in matched:
            ax.scatter(i, i, color="green", s=90)

        elif skill in partial:
            ax.scatter(i, i, color="orange", s=90)

        elif skill in missing:
            ax.scatter(i, i, color="red", s=90)

    ax.set_xticks(range(len(jd_skills)))
    ax.set_xticklabels(jd_skills, rotation=35, ha="right")

    ax.set_yticks(range(len(resume_labels)))
    ax.set_yticklabels(resume_labels)

    ax.set_xlabel("Job Description Skill Groups")
    ax.set_ylabel("Resume Skill Groups")

    ax.grid(True, linestyle="--", alpha=0.4)

    st.pyplot(fig)
