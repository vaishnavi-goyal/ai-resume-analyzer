"""
ats.py
------------------------------------
ATS Score Calculator
Rule-Based Scoring System
"""

import re

# ==========================================================
# DEFAULT KEYWORDS
# ==========================================================

DEFAULT_KEYWORDS = [
    "python",
    "sql",
    "excel",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "keras",
    "power bi",
    "tableau",
    "git",
    "github",
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
]

# ==========================================================
# CALCULATE ATS SCORE
# ==========================================================

def calculate_ats_score(resume_text, job_description):

    if not resume_text:
        return 0

    resume = resume_text.lower()

    if job_description.strip():

        keywords = []

        for word in re.split(r"[,\n]", job_description):

            word = word.strip().lower()

            if len(word) > 2:

                keywords.append(word)

    else:

        keywords = DEFAULT_KEYWORDS

    if len(keywords) == 0:
        return 0

    matched = 0

    for keyword in keywords:

        if keyword in resume:

            matched += 1

    score = int((matched / len(keywords)) * 100)

    if score > 100:
        score = 100

    return score

# ==========================================================
# RESUME RATING
# ==========================================================

def get_resume_rating(score):

    if score >= 90:
        return "⭐⭐⭐⭐⭐ Excellent"

    elif score >= 75:
        return "⭐⭐⭐⭐ Very Good"

    elif score >= 60:
        return "⭐⭐⭐ Good"

    elif score >= 40:
        return "⭐⭐ Average"

    else:
        return "⭐ Needs Improvement"

# ==========================================================
# FEEDBACK
# ==========================================================

def get_feedback(score):

    feedback = []

    if score >= 90:

        feedback.append("Excellent ATS compatibility.")
        feedback.append("Resume is highly optimized.")
        feedback.append("Keep resume updated.")

    elif score >= 75:

        feedback.append("Good ATS Score.")
        feedback.append("Add more job-specific keywords.")
        # ==========================================================
# COMPLETE FEEDBACK
# ==========================================================

    elif score >= 60:

        feedback.append("Your resume is good.")
        feedback.append("Add more technical keywords.")
        feedback.append("Improve your project section.")
        feedback.append("Include measurable achievements.")

    elif score >= 40:

        feedback.append("ATS score is below average.")
        feedback.append("Add relevant skills.")
        feedback.append("Improve resume formatting.")
        feedback.append("Add certifications.")
        feedback.append("Add internship experience.")

    else:

        feedback.append("Resume needs major improvement.")
        feedback.append("Add a professional summary.")
        feedback.append("Include technical skills.")
        feedback.append("Mention projects.")
        feedback.append("Add education details.")
        feedback.append("Use job description keywords.")

    return feedback

# ==========================================================
# CHECK EMAIL
# ==========================================================

def has_email(resume_text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    return bool(re.search(pattern, resume_text))


# ==========================================================
# CHECK PHONE
# ==========================================================

def has_phone(resume_text):

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    return bool(re.search(pattern, resume_text))


# ==========================================================
# CHECK LINKEDIN
# ==========================================================

def has_linkedin(resume_text):

    return "linkedin.com" in resume_text.lower()


# ==========================================================
# CHECK GITHUB
# ==========================================================

def has_github(resume_text):

    return "github.com" in resume_text.lower()


# ==========================================================
# CHECK EXPERIENCE
# ==========================================================

def has_experience(resume_text):

    keywords = [
        "experience",
        "internship",
        "work experience",
        "employment"
    ]

    text = resume_text.lower()

    return any(word in text for word in keywords)


# ==========================================================
# CHECK EDUCATION
# ==========================================================

def has_education(resume_text):

    keywords = [
        "education",
        "bca",
        "b.tech",
        "mca",
        "bachelor",
        "degree",
        "university"
    ]

    text = resume_text.lower()

    return any(word in text for word in keywords)
# ==========================================================
# CHECK PROJECTS
# ==========================================================

def has_projects(resume_text):

    keywords = [
        "project",
        "projects",
        "academic project",
        "personal project",
        "major project",
        "minor project"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)


# ==========================================================
# CHECK CERTIFICATIONS
# ==========================================================

def has_certifications(resume_text):

    keywords = [
        "certificate",
        "certification",
        "certifications",
        "coursera",
        "udemy",
        "forage",
        "google",
        "microsoft",
        "ibm"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)


# ==========================================================
# CHECK SKILLS SECTION
# ==========================================================

def has_skills_section(resume_text):

    keywords = [
        "skills",
        "technical skills",
        "key skills",
        "core skills"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)


# ==========================================================
# CHECK SUMMARY
# ==========================================================

def has_summary(resume_text):

    keywords = [
        "summary",
        "profile",
        "professional summary",
        "career objective",
        "objective"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)


# ==========================================================
# CHECK ACHIEVEMENTS
# ==========================================================

def has_achievements(resume_text):

    keywords = [
        "achievement",
        "achievements",
        "award",
        "awards",
        "winner",
        "rank"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)


# ==========================================================
# CHECK LANGUAGES
# ==========================================================

def has_languages(resume_text):

    keywords = [
        "languages",
        "english",
        "hindi"
    ]

    text = resume_text.lower()

    return any(keyword in text for keyword in keywords)
# ==========================================================
# RESUME SECTION SCORE
# ==========================================================

def resume_section_score(resume_text):

    score = 0

    if has_email(resume_text):
        score += 10

    if has_phone(resume_text):
        score += 10

    if has_linkedin(resume_text):
        score += 5

    if has_github(resume_text):
        score += 5

    if has_summary(resume_text):
        score += 10

    if has_skills_section(resume_text):
        score += 15

    if has_projects(resume_text):
        score += 15

    if has_experience(resume_text):
        score += 10

    if has_education(resume_text):
        score += 10

    if has_certifications(resume_text):
        score += 5

    if has_achievements(resume_text):
        score += 3

    if has_languages(resume_text):
        score += 2

    return min(score, 100)


# ==========================================================
# FINAL RESUME SCORE
# ==========================================================

def calculate_final_resume_score(resume_text, job_description):

    ats_score = calculate_ats_score(
        resume_text,
        job_description
    )

    section_score = resume_section_score(
        resume_text
    )

    final_score = int(
        (ats_score * 0.7) +
        (section_score * 0.3)
    )

    return min(final_score, 100)


# ==========================================================
# RESUME GRADE
# ==========================================================

def get_resume_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 50:
        return "D"

    else:
        return "F"


# ==========================================================
# IMPROVEMENT TIPS
# ==========================================================

def improvement_tips(resume_text):

    tips = []

    if not has_summary(resume_text):
        tips.append("Add a professional summary.")

    if not has_skills_section(resume_text):
        tips.append("Include a dedicated Skills section.")

    if not has_projects(resume_text):
        tips.append("Add your academic or personal projects.")

    if not has_experience(resume_text):
        tips.append("Mention internships or work experience.")

    if not has_certifications(resume_text):
        tips.append("Add relevant certifications.")

    if not has_linkedin(resume_text):
        tips.append("Include your LinkedIn profile.")

    if not has_github(resume_text):
        tips.append("Include your GitHub profile.")

    if not has_achievements(resume_text):
        tips.append("Highlight your achievements.")

    if not has_languages(resume_text):
        tips.append("Mention the languages you know.")

    return tips
