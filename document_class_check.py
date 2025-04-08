def classify_document(content: str) -> str:
    if "invoice" in content.lower():
        return "Invoice"
    elif "report" in content.lower():
        return "Report"
    elif "meeting" in content.lower():
        return "Meeting Notes"
    else:
        return "General Document"
