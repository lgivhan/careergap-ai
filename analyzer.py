import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models import GapAnalysis

load_dotenv()

def analyze_gap(resume_text, jd_text):
    print("🧠 AI is analyzing your career gap...")
    
    # 1. Initialize the Brain (using the cheaper, faster gpt-4o-mini)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # 2. Bind the schema so the output is ALWAYS structured
    structured_llm = llm.with_structured_output(GapAnalysis)
    
    # 3. Define the Prompt (The "Instructions")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a lead technical recruiter at PwC. Compare the user's resume to the job description. Be critical, honest, and look for technical gaps."),
        ("user", "RESUME:\n{resume}\n\nJOB DESCRIPTION:\n{jd}")
    ])
    
    # 4. Run the chain
    chain = prompt | structured_llm
    return chain.invoke({"resume": resume_text, "jd": jd_text})