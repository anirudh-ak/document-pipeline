from docx import Document

def read_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    except Exception as e:
        raise RuntimeError(f"Error reading DOCX file: {e}")
