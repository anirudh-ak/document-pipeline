import os
import sys
import openai
from jinja2 import Environment, FileSystemLoader
from document_reader.docx_reader import read_docx
from document_reader.pdf_reader import read_pdf
from document_class_check import classify_document
from summarize_document import summarize_text

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_document(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

def build_summary_prompt(content: str) -> str:
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("summary_prompt.jinja2")
    return template.render(document_text=content)

def run(file_path: str):
    print(f"\n📄 Reading document: {file_path}")
    content = read_document(file_path)

    print("🔎 Classifying document type...")
    doc_type = classify_document(content)
    print(f"➡️  Detected type: {doc_type}")

    print("🧠 Building summary prompt...")
    prompt = build_summary_prompt(content)

    print("💬 Calling OpenAI for summary...")
    summary = summarize_text(content, prompt)

    print("\n✅ Summary:\n")
    print(summary)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_agentic_flow.py <path_to_document>")
    else:
        run(sys.argv[1])
