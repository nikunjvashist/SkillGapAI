from PyPDF2 import PdfReader
import docx

def load_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join(page.extract_text() or "" for page in reader.pages)

    if file.name.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)

    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    return ""
