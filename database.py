import os
from dotenv import load_dotenv
from supabase import create_client

# Load the variables from .env
load_dotenv()

def get_db():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

if __name__ == "__main__":
    try:
        supabase = get_db()
        # This just checks if the table exists by trying to select from it
        supabase.table("analysis_history").select("*").limit(1).execute()
        print("✅ SUCCESS: Python is connected to Supabase!")
    except Exception as e:
        print(f"❌ ERROR: Connection failed: {e}")