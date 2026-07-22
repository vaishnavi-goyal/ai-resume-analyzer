"""
ai_feedback.py
------------------------------------
Resume Feedback Module
"""

# ==========================================================
# RESUME SUMMARY
# ==========================================================

def generate_summary(resume_text):

    words = resume_text.split()

    if len(words) <= 40:
        return resume_text

    return " ".join(words[:40]) + "..."


# ==========================================================
# RESUME STRENGTH
# ==========================================================

def resume_strength(resume_text):

    words = len(resume_text.split())

    if words >= 500:
        return "Excellent"

    elif words >= 350:
        return "Good"

    elif words >= 200:
        return "Average"

    return "Weak"


# ==========================================================
# COMPLETENESS SCORE
# ==========================================================

def completeness_score(resume_text):

    score = 0

    text = resume_text.lower()

    sections = [

        "summary",
        "education",
        "skills",
        "projects",
        "experience",
        "certification"

    ]

    for section in sections:

        if section in text:

            score += 100 / len(sections)

    return int(score)


# ==========================================================
# RECOMMENDED ROLES
# ==========================================================

def recommend_roles(found_skills):

    roles = []

    skills = [s.lower() for s in found_skills]

    if "python" in skills and "machine learning" in skills:
        roles.append("Machine Learning Engineer")

    if "sql" in skills and "excel" in skills:
        roles.append("Data Analyst")

    if "power bi" in skills:
        roles.append("Business Intelligence Analyst")

    if "streamlit" in skills:
        roles.append("Python Developer")

    if "html" in skills and "css" in skills:
        roles.append("Frontend Developer")

    return roles
# ==========================================================
# CHECK RESUME SECTIONS
# ==========================================================

def check_resume_sections(resume_text):

    text = resume_text.lower()

    sections = {

        "Summary": "summary" in text or "objective" in text,

        "Education": "education" in text,

        "Skills": "skills" in text,

        "Projects": "project" in text,

        "Experience": "experience" in text or "internship" in text,

        "Certifications": "certification" in text or "certificate" in text

    }

    return sections


# ==========================================================
# RESUME FEEDBACK
# ==========================================================

def resume_feedback(resume_text):

    feedback = []

    sections = check_resume_sections(resume_text)

    for section, present in sections.items():

        if not present:

            feedback.append(f"Add {section} section.")

    if len(resume_text.split()) < 250:

        feedback.append("Resume is too short. Add more relevant content.")

    elif len(resume_text.split()) > 700:

        feedback.append("Resume is too long. Keep it within 1-2 pages.")

    else:

        feedback.append("Resume length looks good.")

    return feedback


# ==========================================================
# IMPROVEMENT SUGGESTIONS
# ==========================================================

def improvement_suggestions(resume_text):

    suggestions = []

    text = resume_text.lower()

    if "github.com" not in text:

        suggestions.append("Add your GitHub profile.")

    if "linkedin.com" not in text:

        suggestions.append("Add your LinkedIn profile.")

    if "project" not in text:

        suggestions.append("Include at least 2 projects.")

    if "certificate" not in text:

        suggestions.append("Add your certifications.")

    if "achievement" not in text:

        suggestions.append("Mention achievements or awards.")

    return suggestions


# ==========================================================
# CAREER TIPS
# ==========================================================

def career_tips():

    return [

        "Keep your resume updated.",

        "Customize resume for every job.",

        "Use ATS-friendly keywords.",

        "Show measurable achievements.",

        "Keep formatting simple.",

        "Mention technical skills clearly.",

        "Add internships and projects.",

        "Proofread before applying."

    ]
