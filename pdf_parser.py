from pypdf import PdfReader

def extract_resume_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return "\n".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        print(f"❌ Resume Error: {e}")
        return None