from pydantic import BaseModel, Field
from typing import List, Optional

class GapAnalysis(BaseModel):
    """The structured result of the AI's resume-to-job comparison."""
    job_title: str = Field(description="The formal job title from the job description.")
    company_name: str = Field(description="The name of the company.")
    match_score: int = Field(description="Match score from 0-100.")
    missing_skills: List[str] = Field(description="Technical skills in job description but not resume.")
    recommended_project: str = Field(description="A specific, actionable project to bridge the gap.")
    explanation: str = Field(description="A short 2-sentence summary of the match logic.")
    source_url: Optional[str] = None