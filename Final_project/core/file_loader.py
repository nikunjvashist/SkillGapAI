import pdfplumber
import docx

def load_file(file):
    ext = file.name.split(".")[-1].lower()

    if ext == "txt":
        return file.read().decode("utf-8", errors="ignore")

    elif ext == "pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + " "
        return text

    elif ext == "docx":
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)

    else:
        raise ValueError("Unsupported file format")
