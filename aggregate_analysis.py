import os
from collections import Counter
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from database import get_db

load_dotenv()

def run_aggregate_report():
    client = get_db()
    if not client: return

    print("📊 Fetching all historical analyses from Supabase...")
    
    # 1. Pull all missing_skills from your table
    response = client.table("job_analyses").select("missing_skills").execute()
    all_records = response.data

    if not all_records:
        print("❌ No data found in the database yet.")
        return

    # 2. Flatten the list of lists into one big list of skills
    all_missing_skills = []
    for record in all_records:
        all_missing_skills.extend(record.get('missing_skills', []))

    # 3. Count frequencies
    skill_counts = Counter(all_missing_skills)
    top_skills = [skill for skill, count in skill_counts.most_common(3)]
    
    print(f"✅ Analyzed {len(all_records)} job postings.")
    print(f"🔥 Top 3 Missing Skills: {', '.join(top_skills)}")

    # 4. Ask AI to design a 'Master Project' for these specific skills
    print("\n🧠 AI is architecting a Master Project to bridge these gaps...")
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a senior career coach and software architect."),
        ("user", "Based on these top missing technical skills: {skills}, suggest one high-impact project to gain and experience in 50 words or less.")
    ])

    chain = prompt | llm
    recommendation = chain.invoke({"skills": ", ".join(top_skills)})

    # 5. Output the result
    print("\n" + "═"*60)
    print("🚀 STRATEGIC CAREER ROADMAP")
    print("═"*60)
    print(recommendation.content)
    print("═"*60)

if __name__ == "__main__":
    run_aggregate_report()