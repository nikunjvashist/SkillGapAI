import PyPDF2
import pdfplumber
import re

pdf_path = "your.pdf"


# 1. Extract ALL text from the PDF using PyPDF2

def extract_all_text_pypdf2(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

all_text = extract_all_text_pypdf2(pdf_path)
print("\n--- 1. All Text (PyPDF2) ---")
print(all_text)


# 2. Extract text only from Page 1

def extract_page1(path):
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return reader.pages[0].extract_text() or ""

page1_text = extract_page1(pdf_path)
print("\n--- 2. Page 1 Text ---")
print(page1_text)



# 3. Count total pages in PDF

def count_pages(path):
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return len(reader.pages)

total_pages = count_pages(pdf_path)
print("\n--- 3. Total Pages ---")
print(total_pages)


# 4. Detect whether PDF is scanned
#    (If text extraction is empty → scanned)

def is_scanned(text):
    return len(text.strip()) == 0

print("\n--- 4. Scanned PDF? ---")
print("Yes, scanned" if is_scanned(all_text) else "Not scanned")



# 5. Extract Headings (uppercase lines)

def extract_headings(text):
    headings = []
    for line in text.split("\n"):
        if line.strip() and line.isupper():
            headings.append(line)
    return headings

headings = extract_headings(all_text)
print("\n--- 5. Headings ---")
print(headings)



# 6. Extract tables using pdfplumber

def extract_tables(path):
    tables = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            tbl = page.extract_table()
            if tbl:
                tables.append(tbl)
    return tables

tables = extract_tables(pdf_path)
print("\n--- 6. Extracted Tables ---")
print(tables)


# 7. Extract metadata (Author, Title, Creation Date)

def extract_metadata(path):
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        metadata = reader.metadata
    return {
        "Author": metadata.author,
        "Title": metadata.title,
        "CreationDate": metadata.creation_date
    }

metadata = extract_metadata(pdf_path)
print("\n--- 7. Metadata ---")
print(metadata)


# 8. Save extracted text to .txt file

with open("extracted_output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("\n--- 8. Text saved to extracted_output.txt ---")



# 9. Extract only Email IDs using regex

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

emails = extract_emails(all_text)
print("\n--- 9. Emails ---")
print(emails)



# 10. Combined Extractor:
#     Try PyPDF2 → if empty → try pdfplumber
#     If still empty → Scanned PDF

def combined_extractor(path):
    print("\n--- 10. Combined Extractor ---")

    # Try PyPDF2 first
    pypdf2_text = extract_all_text_pypdf2(path)
    if pypdf2_text.strip():
        print("Extracted using PyPDF2")
        return pypdf2_text

    # If empty → try pdfplumber
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    if text.strip():
        print("Extracted using pdfplumber")
        return text

    # If still empty → scanned
    print("Scanned PDF detected")
    return ""

combined_text = combined_extractor(pdf_path)
print(combined_text)
