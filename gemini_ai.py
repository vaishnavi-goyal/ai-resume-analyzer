import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")
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

# ==========================================================
# AI COVER LETTER
# ==========================================================

def generate_cover_letter(resume_text, job_description):

    prompt = f"""
Write a professional cover letter.

Resume:
{resume_text}

Job Description:
{job_description}

Make it ATS friendly and professional.
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# AI RESUME REWRITER
# ==========================================================

def rewrite_resume(resume_text, job_description):

    prompt = f"""
Rewrite the following resume professionally.

Improve:

- ATS Score
- Formatting
- Keywords
- Skills
- Professional Summary

Resume:

{resume_text}

Job Description:

{job_description}

Return only the improved resume.
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# MOCK INTERVIEW
# ==========================================================

def generate_interview_questions(resume_text, job_description):

    prompt = f"""
Generate 10 interview questions.

Resume:
{resume_text}

Job Description:
{job_description}

Return only questions.
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# COMPANY MATCH
# ==========================================================

def company_match(resume_text, job_description):

    prompt = f"""
Based on this resume recommend 10 companies.

Resume:
{resume_text}

Job Description:
{job_description}

Return only company names with one-line reason.
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# CAREER ROADMAP
# ==========================================================

def career_roadmap(found_skills, missing_skills):

    prompt = f"""
Create a career roadmap.

Current Skills:
{found_skills}

Missing Skills:
{missing_skills}

Return:

30 Days Plan

60 Days Plan

90 Days Plan

Projects

Certificates

Interview Preparation
"""

    response = model.generate_content(prompt)

    return response.text
