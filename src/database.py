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
    
    # GUARD CLAUSE - Get current user before building the payload
    user_response = client.auth.get_user()
    if not user_response.user:
        print("❌ AUTH ERROR: No logged-in user found. RLS will block this insert.")
        return
    
    user_id = user_response.user.id

    data = {
        "user_id": user_id,
        "job_title": analysis.job_title,
        "company_name": analysis.company_name,
        "match_score": analysis.match_score,
        "missing_skills": analysis.missing_skills,
        "recommended_project": analysis.recommended_project,
        "explanation": analysis.explanation,
        "source_url": analysis.source_url
    }
    
    try:
        response = client.table("job_analyses").insert(data).execute()
        print("✅ SUCCESS: Analysis saved to job_analyses table!")
        return response
    except Exception as e:
        print(f"❌ DATABASE ERROR: {e}")

if __name__ == "__main__":
    client = get_db()
    if client:
        try:
            client.table("job_analyses").select("*").limit(1).execute()
            print("✅ CONNECTION SUCCESSFUL: Ready to log job analyses.")
        except Exception as e:
            print(f"❌ CONNECTION FAILED: {e}")