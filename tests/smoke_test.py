import os
from dotenv import load_dotenv
from pypdf import PdfReader
from supabase import create_client

def run_smoke_test():
    load_dotenv()
    print("🚀 Starting CareerGap AI Smoke Test...\n")

    # 1. Check Environment Variables
    keys = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_KEY"]
    for key in keys:
        if os.getenv(key):
            print(f"✅ {key} found.")
        else:
            print(f"❌ {key} MISSING.")

    # 2. Check PDF Ingestion
    try:
        reader = PdfReader("my_resume.pdf")
        text = reader.pages[0].extract_text()
        if len(text) > 0:
            print("✅ PDF Ingestion working (Resume found and readable).")
    except Exception as e:
        print(f"❌ PDF Ingestion FAILED: {e}")

    # 3. Check Supabase Connection
    try:
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        supabase = create_client(url, key)
        # Attempt a simple "count" query to verify connection
        supabase.table("analyses").select("id", count="exact").limit(1).execute()
        print("✅ Supabase connection successful.")
    except Exception as e:
        print(f"❌ Supabase Connection FAILED: {e}")

    print("\n--- Smoke Test Complete ---")

if __name__ == "__main__":
    run_smoke_test()