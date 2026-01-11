import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models import GapAnalysis

load_dotenv()

def analyze_gap(resume_text, jd_text, url):
    print("🧠 AI is analyzing your career gap...")
    
    # 1. Initialize the AI
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # 2. Bind the schema to structured the output
    structured_llm = llm.with_structured_output(GapAnalysis)
    
    # 3. Define the Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a lead technical recruiter. Compare the user's resume to the job description. Be critical, honest, and look for technical gaps."),
        ("user", "RESUME:\n{resume}\n\nJOB DESCRIPTION:\n{jd}")
    ])
    
    # 4. Run the chain
    chain = prompt | structured_llm

    # 5. Get the AI analysis
    report = chain.invoke({"resume": resume_text, "jd": jd_text})

    # 6. Attach the URL metadata to the object before returning it
    report.source_url = url

    return report