import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume against the job description.

Return your answer in this format:

ATS Score: XX%

Strengths:
- ...

Missing Skills:
- ...

Suggestions:
- ...

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = model.generate_content(prompt)

    return response.text