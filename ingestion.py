import sys

def get_job_details():
    """Single source of truth for capturing job data via terminal."""
    print("\n" + "═"*50)
    print(" 🚀 CAREERGAP AI: JOB INPUT")
    print("="*50)
    
    company = input("🏢 Company Name: ")
    title = input("💼 Job Title: ")
    
    print("\n📝 Paste the Job Description & Requirements below.")
    print("👉 (When done: Press Enter, then Ctrl-D on Mac or Ctrl-Z on Win)")
    print("-" * 20)
    
    jd_body = sys.stdin.read()
    
    return {
        "company": company,
        "title": title,
        "description": jd_body.strip()
    }