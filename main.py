import sys
from pdf_parser import extract_resume_text
from ingestion import get_job_details
from analyzer import analyze_gap
from database import save_analysis

if __name__ == "__main__":
    # 1. GATHER
    resume_text = extract_resume_text("my_resume.pdf")
    job_data = get_job_details()
    
    if resume_text and job_data['description']:
        # 2. ANALYZE
        report = analyze_gap(resume_text, job_data['description'], job_data['url'])
        
        # 3. DISPLAY RESULTS
        print("\n" + "📊" * 15)
        print(f"REPORT FOR: {report.job_title} at {job_data['company']}")
        print(f"MATCH SCORE: {report.match_score}%")
        print("-" * 30)
        print(f"🛠  MISSING SKILLS: {', '.join(report.missing_skills)}")
        print(f"💡 PROJECT IDEA: {report.recommended_project}")
        print(f"📝 SUMMARY: {report.explanation}")
        print("📊" * 15 + "\n")
        
        # 4. SAVE TO DATABASE
        save_analysis(report)