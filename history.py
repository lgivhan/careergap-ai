from src.database import get_db

def search_history(query=None, limit=5):
    client = get_db()
    if not client: return
    
    # 🕵️‍♂️ The "Professional" approach: Filter in the database, not in Python
    print(f"\n🔍 SEARCHING HISTORY FOR: '{query or 'All'}'...")
    
    # Build the query
    db_query = client.table("job_analyses").select("*").order("created_at", desc=True)
    
    if query:
        # Searches for the query string within the company_name column (case-insensitive)
        db_query = db_query.ilike("company_name", f"%{query}%")
    
    response = db_query.limit(limit).execute()
    analyses = response.data
    
    if not analyses:
        print(f"No records found matching '{query}'.")
        return

    for entry in analyses:
        print("\n" + "═"*40)
        print(f"🏢 COMPANY: {entry['company_name']}")
        print(f"💼 ROLE:    {entry['job_title']}")
        print(f"📊 SCORE:   {entry['match_score']}%")
        print(f"🔗 URL:     {entry.get('source_url', 'N/A')}")
        print(f"💡 PROJECT: {entry['recommended_project']}")
        print("═"*40)

if __name__ == "__main__":
    # Example: Run without args for all, or pass a string to search
    import sys
    search_term = sys.argv[1] if len(sys.argv) > 1 else None
    search_history(search_term)