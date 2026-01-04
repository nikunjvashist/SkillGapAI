import matplotlib.pyplot as plt
import streamlit as st

from skill_matching.skill_groups import (
    RESUME_SKILL_GROUPS,
    JD_SKILL_GROUPS
)


def render_similarity_matrix(matrix_points):
    """
    Renders a reference-style similarity matrix (bubble chart)
    using skill groups instead of raw skills.
    """

    fig, ax = plt.subplots(figsize=(8, 4.5))

    # Color and size mapping (as per reference UI)
    color_map = {
        "high": "#6BC96B",     # green
        "partial": "#F4B400",  # orange
        "low": "#E5533D"       # red
    }

    size_map = {
        "high": 220,
        "partial": 160,
        "low": 120
    }

    # Plot each matrix point safely
    for item in matrix_points:

        # SAFETY CHECK (prevents crashes forever)
        if (
            item.get("x") not in JD_SKILL_GROUPS
            or item.get("y") not in RESUME_SKILL_GROUPS
            or item.get("status") not in color_map
        ):
            continue

        x_index = JD_SKILL_GROUPS.index(item["x"])
        y_index = RESUME_SKILL_GROUPS.index(item["y"])

        ax.scatter(
            x_index,
            y_index,
            s=size_map[item["status"]],
            color=color_map[item["status"]],
            edgecolors="none"
        )

    # X-axis (JD Skills)
    ax.set_xticks(range(len(JD_SKILL_GROUPS)))
    ax.set_xticklabels(JD_SKILL_GROUPS, rotation=30, ha="right")

    # Y-axis (Resume Skills)
    ax.set_yticks(range(len(RESUME_SKILL_GROUPS)))
    ax.set_yticklabels(RESUME_SKILL_GROUPS)

    ax.set_xlabel("Job Description Skill Groups")
    ax.set_ylabel("Resume Skill Groups")
    ax.set_title("Similarity Matrix")

    # Grid styling (reference-like)
    ax.grid(True, linestyle="--", alpha=0.3)

    st.pyplot(fig)
