import matplotlib.pyplot as plt
import streamlit as st

def render_skill_donut(matched, partial, missing):
    labels = ["Matched", "Partial", "Missing"]
    values = [matched, partial, missing]
    colors = ["green", "orange", "red"]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")

    st.pyplot(fig)
