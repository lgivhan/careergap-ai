import sys
from pdf_parser import extract_resume_text
from analyzer import analyze_gap  # Import your AI "Brain"

def get_job_details():
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
        "description": jd_body
    }

if __name__ == "__main__":
    # 1. GATHER DATA
    resume_text = extract_resume_text("my_resume.pdf")
    job_data = get_job_details()
    
    if resume_text and job_data['description']:
        # 2. ANALYZE DATA (Phase 3)
        # We pass the cleaned inputs to our analyzer
        report = analyze_gap(resume_text, job_data['description'])
        
        # 3. DISPLAY RESULTS
        print("\n" + "📊" * 15)
        print(f"REPORT FOR: {report.job_title} at {job_data['company']}")
        print(f"MATCH SCORE: {report.match_score}%")
        print("-" * 30)
        print(f"🛠  MISSING SKILLS: {', '.join(report.missing_skills)}")
        print(f"💡 PROJECT IDEA: {report.recommended_project}")
        print(f"📝 SUMMARY: {report.explanation}")
        print("📊" * 15 + "\n")
        
        # TODO: Phase 4 - Save this report to Supabase