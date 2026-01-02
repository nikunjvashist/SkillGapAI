import matplotlib.pyplot as plt
import streamlit as st

def show_skill_chart(tech_count, soft_count):
    labels = ["Technical Skills", "Soft Skills"]
    sizes = [tech_count, soft_count]

    fig, ax = plt.subplots()
    ax.pie(
        sizes,
        labels=labels,
        startangle=90,
        autopct="%1.0f%%",
        wedgeprops=dict(width=0.4)
    )
    ax.axis("equal")

    st.pyplot(fig)
