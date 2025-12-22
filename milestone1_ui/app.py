import streamlit as st

from parserspdf_parser import extract_text_from_pdf
from parsersdocx_parser import extract_text_from_docx
from parserstxt_parser import extract_text_from_txt
from cleanerstext_cleaner import clean_text


st.set_page_config(layout="wide")
st.title("Milestone 1: Data Ingestion and Parsing Module")

left, right = st.columns(2)

def extract_text(file):
    if not file:
        return ""
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    if file.type == "text/plain":
        return extract_text_from_txt(file)
    if file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file)
    return ""

with left:
    st.subheader("Upload Documents")
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    job_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

with right:
    st.subheader("Preview")
    tab1, tab2 = st.tabs(["Resume", "Job Description"])

    resume_text = clean_text(extract_text(resume_file))
    job_text = clean_text(extract_text(job_file))

    with tab1:
        st.text_area("Cleaned Resume", resume_text[:3000], height=350)

    with tab2:
        st.text_area("Cleaned Job Description", job_text[:3000], height=350)
