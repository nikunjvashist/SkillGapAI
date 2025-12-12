# pdf_final_numbered.py
import sys
from pathlib import Path
import pdfplumber
import pandas as pd
try:
    import fitz
    HAS_FITZ = True
except:
    HAS_FITZ = False


# -------------------- 1) Extract text from FIRST page --------------------
def q1_page1_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return (pdf.pages[0].extract_text() or "") if pdf.pages else ""


# -------------------- 2) Extract ALL text from PDF --------------------
def q2_all_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(p.extract_text() or "" for p in pdf.pages)


# -------------------- 3) Count total pages --------------------
def q3_page_count(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return len(pdf.pages)


# -------------------- 4) Detect scanned PDF (empty text) --------------------
def q4_is_scanned(text):
    return not bool(text.strip())


# -------------------- 5) Extract FIRST table on Page 1 --------------------
def q5_first_table_page1(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        if not pdf.pages: return None
        tables = pdf.pages[0].extract_tables() or []
        return tables[0] if tables else None


# -------------------- 6) Extract ALL tables from PDF --------------------
def q6_all_tables(pdf_path):
    all_tbl = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            for t in (page.extract_tables() or []):
                all_tbl.append({"page": i, "table": t})
    return all_tbl


# -------------------- 7) Extract all words + bounding boxes --------------------
def q7_words_bboxes(pdf_path):
    out = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            for w in page.extract_words():
                out.append({
                    "page": i,
                    "text": w.get("text"),
                    "x0": w.get("x0"),
                    "x1": w.get("x1"),
                    "top": w.get("top"),
                    "bottom": w.get("bottom")
                })
    return out


# -------------------- 8) Extract images from PDF --------------------
def q8_extract_images(pdf_path, out_dir="images"):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    saved = []
    if HAS_FITZ:
        doc = fitz.open(pdf_path)
        for p in range(len(doc)):
            for idx, img in enumerate(doc.get_page_images(p), start=1):
                xref = img[0]
                base = doc.extract_image(xref)
                ext = base.get("ext", "png")
                name = out_dir / f"page{p+1}_img{idx}.{ext}"
                with open(name, "wb") as f:
                    f.write(base["image"])
                saved.append(str(name))
        doc.close()
    return saved


# -------------------- 9) Extract vector objects (lines, rects, curves) --------------------
def q9_vector_objects(pdf_path):
    vect = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            objs = getattr(page, "objects", {}) or {}
            for key in ("lines", "rects", "curves"):
                for o in objs.get(key, []):
                    vect.append({"page": i, "type": key, "object": o})
    return vect


# -------------------- 10) Save a table as CSV --------------------
def q10_save_table_csv(pdf_path, out_csv="extracted_table.csv"):
    with pdfplumber.open(pdf_path) as pdf:
        # Page 1 first
        if pdf.pages:
            t = pdf.pages[0].extract_tables() or []
            if t:
                df = pd.DataFrame(t[1:], columns=t[0]) if len(t) > 1 else pd.DataFrame(t)
                df.to_csv(out_csv, index=False)
                return out_csv
        # Scan full PDF
        for p in pdf.pages:
            t = p.extract_tables() or []
            if t:
                df = pd.DataFrame(t[1:], columns=t[0]) if len(t) > 1 else pd.DataFrame(t)
                df.to_csv(out_csv, index=False)
                return out_csv
    return None
