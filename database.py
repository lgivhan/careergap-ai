import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

def get_db():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    # 🕵️‍♂️ Professional Debugging
    if not url or not key:
        print("❌ ERROR: .env variables are missing!")
        return None
    
    # Check for common mistakes
    if url.endswith('/'):
        print("⚠️ WARNING: Your URL has a trailing slash. Removing it...")
        url = url.rstrip('/')
    
    print(f"📡 Project URL: {url}")
    print(f"🔑 Key Prefix: {key[:15]}...") # Verify it starts with sb_publishable_
    
    return create_client(url, key)

if __name__ == "__main__":
    client = get_db()
    if client:
        try:
            # Try a simple health check
            client.table("analysis_history").select("*").limit(1).execute()
            print("✅ SUCCESS: Connected to Supabase with the new Publishable Key!")
        except Exception as e:
            print(f"❌ CONNECTION FAILED: {e}")