import fitz  # PyMuPDF

def read_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file: {e}")
