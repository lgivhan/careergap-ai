import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

def get_db():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        print("❌ ERROR: .env variables are missing!")
        return None
    
    if url.endswith('/'):
        url = url.rstrip('/')
    
    return create_client(url, key)

def save_analysis(analysis):
    client = get_db()
    if not client:
        return
    
    # This dictionary exactly matches the columns in your screenshot for 'job_analyses'
    data = {
        "job_title": analysis.job_title,
        "company_name": analysis.company_name,
        "match_score": analysis.match_score,
        "missing_skills": analysis.missing_skills,
        "recommended_project": analysis.recommended_project,
        "explanation": analysis.explanation,
        "source_url": analysis.source_url
    }
    
    try:
        # UPDATED: Pointing to the table with match_score and explanation
        response = client.table("job_analyses").insert(data).execute()
        print("✅ SUCCESS: Analysis saved to job_analyses table!")
        return response
    except Exception as e:
        print(f"❌ DATABASE ERROR: {e}")

if __name__ == "__main__":
    client = get_db()
    if client:
        try:
            # UPDATED: Health check now targets the correct table
            client.table("job_analyses").select("*").limit(1).execute()
            print("✅ CONNECTION SUCCESSFUL: Ready to log job analyses.")
        except Exception as e:
            print(f"❌ CONNECTION FAILED: {e}")