import sys
from pdf_parser import extract_resume_text

def get_job_details():
    print("\n" + "═"*50)
    print(" 💼 JOB DATA ENTRY (Clean Signal Mode)")
    print("="*50)
    
    company = input("🏢 Company Name: ")
    title = input("💼 Job Title: ")
    
    print("\n📝 Paste the Job Description (Responsibilities/Requirements) below.")
    print("👉 (Press Enter, then Ctrl-D on Mac or Ctrl-Z on Win when done)")
    print("-" * 20)
    
    # This grabs multiple lines of text until the user hits the "End of File" command
    jd_body = sys.stdin.read()
    
    return {
        "company": company,
        "title": title,
        "description": jd_body.strip()
    }

if __name__ == "__main__":
    # Test the combined flow
    print("📄 Reading local resume...")
    resume_text = extract_resume_text("my_resume.pdf")
    
    if not resume_text:
        print("❌ Error: Could not find or read 'my_resume.pdf'.")
        sys.exit()

    job_data = get_job_details()
    
    print("\n" + "✅" * 10)
    print("DATA PIPELINE READY")
    print(f"Resume Length: {len(resume_text)} chars")
    print(f"Job Description Length: {len(job_data['description'])} chars")