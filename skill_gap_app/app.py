import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from docx import Document
import io

# ==============================
# SESSION STATE INITIALIZATION
# ==============================
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "jd_text" not in st.session_state:
    st.session_state.jd_text = ""
if "results" not in st.session_state:
    st.session_state.results = None

# ==============================
# BASIC APP UI
# ==============================
st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")

st.title("📊 Skill Gap Analysis Dashboard")
st.write(
    "Upload a **Resume** and a **Job Description** to analyze skill matching, "
    "identify gaps, and export results."
)

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Navigation")
st.sidebar.write("• Upload Files")
st.sidebar.write("• Preview Text")
st.sidebar.write("• Skill Analysis")
st.sidebar.write("• Visualization")
st.sidebar.write("• Export Report")

# ==============================
# HELPER FUNCTIONS
# ==============================
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def read_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def read_txt(file):
    return file.read().decode("utf-8")

def load_file(file):
    if file.name.endswith(".pdf"):
        return read_pdf(file)
    elif file.name.endswith(".docx"):
        return read_docx(file)
    elif file.name.endswith(".txt"):
        return read_txt(file)
    else:
        raise ValueError("Unsupported file format")

# ==============================
# FILE UPLOADERS
# ==============================
st.subheader("📤 Upload Files")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

with col2:
    jd_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

# ==============================
# LOAD FILES WITH ERROR HANDLING
# ==============================
if resume_file:
    try:
        st.session_state.resume_text = load_file(resume_file)
        st.success(f"Resume Uploaded: {resume_file.name}")
    except Exception as e:
        st.error(str(e))

if jd_file:
    try:
        st.session_state.jd_text = load_file(jd_file)
        st.success(f"Job Description Uploaded: {jd_file.name}")
    except Exception as e:
        st.error(str(e))

# ==============================
# PREVIEW SECTION
# ==============================
st.subheader("📄 File Preview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Resume Preview")
    if st.session_state.resume_text:
        st.text(st.session_state.resume_text[:300])
    else:
        st.warning("No resume uploaded")

with col2:
    st.markdown("### Job Description Preview")
    if st.session_state.jd_text:
        st.text(st.session_state.jd_text[:300])
    else:
        st.warning("No job description uploaded")

# ==============================
# PROCESS BUTTON
# ==============================
if st.button("🚀 Analyze Skills"):
    if not st.session_state.resume_text or not st.session_state.jd_text:
        st.error("Please upload both Resume and Job Description")
    else:
        # ==============================
        # SKILL LIST (SAMPLE)
        # ==============================
        SKILLS = [
            "python", "sql", "machine learning", "data analysis",
            "communication", "leadership", "statistics", "nlp"
        ]

        resume_text = st.session_state.resume_text.lower()
        jd_text = st.session_state.jd_text.lower()

        matched = []
        missing = []
        similarity_data = []

        for skill in SKILLS:
            in_resume = skill in resume_text
            in_jd = skill in jd_text

            if in_resume and in_jd:
                matched.append(skill)
                score = 1.0
            elif in_jd and not in_resume:
                missing.append(skill)
                score = 0.0
            else:
                score = 0.5 if in_resume else 0.0

            similarity_data.append({"Skill": skill, "Similarity": score})

        match_percentage = int((len(matched) / len(SKILLS)) * 100)

        st.session_state.results = {
            "matched": matched,
            "missing": missing,
            "percentage": match_percentage,
            "table": pd.DataFrame(similarity_data)
        }

# ==============================
# RESULTS DISPLAY
# ==============================
if st.session_state.results:
    results = st.session_state.results

    st.subheader("📈 Skill Match Summary")

    st.metric(
        label="Skill Match Percentage",
        value=f"{results['percentage']}%"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Matched Skills")
        st.write(results["matched"])

    with col2:
        st.markdown("### ❌ Missing Skills")
        st.write(results["missing"])

    # ==============================
    # BAR CHART
    # ==============================
    st.subheader("📊 Skills Comparison Chart")

    fig, ax = plt.subplots()
    ax.bar(
        ["Matched Skills", "Missing Skills"],
        [len(results["matched"]), len(results["missing"])]
    )
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # ==============================
    # SIMILARITY TABLE
    # ==============================
    st.subheader("📋 Skill Similarity Table")
    st.dataframe(results["table"])

    # ==============================
    # DOWNLOAD CSV
    # ==============================
    st.subheader("⬇️ Export Results")

    csv_buffer = io.StringIO()
    results["table"].to_csv(csv_buffer, index=False)

    st.download_button(
        label="Download Skill Gap Report (CSV)",
        data=csv_buffer.getvalue(),
        file_name="skill_gap_report.csv",
        mime="text/csv"
    )
