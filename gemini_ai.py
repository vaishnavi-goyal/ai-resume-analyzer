import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS recruiter.

Analyze this resume.

Resume:
{resume_text}

Job Description:
{job_description}

Return:
1. ATS Analysis
2. Strengths
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions
6. Final Rating (/10)
"""

    response = model.generate_content(prompt)

    return response.text