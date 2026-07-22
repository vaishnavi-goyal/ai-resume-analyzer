"""
skills.py
------------------------------------
Skills Detection Module
"""

from config import TECH_SKILLS

# ==========================================================
# DETECT SKILLS
# ==========================================================

def detect_skills(resume_text):

    if not resume_text:
        return []

    text = resume_text.lower()

    detected = []

    for skill in TECH_SKILLS:

        if skill.lower() in text:

            detected.append(skill)

    detected = sorted(list(set(detected)))

    return detected


# ==========================================================
# GET MISSING SKILLS
# ==========================================================

def get_missing_skills(found_skills, job_description):

    if not job_description.strip():

        return []

    jd = job_description.lower()

    required = []

    for skill in TECH_SKILLS:

        if skill.lower() in jd:

            required.append(skill)

    missing = []

    for skill in required:

        if skill not in found_skills:

            missing.append(skill)

    return sorted(missing)


# ==========================================================
# TOTAL SKILLS
# ==========================================================

def count_skills(found_skills):

    return len(found_skills)


# ==========================================================
# SKILL MATCH %
# ==========================================================

def skill_match_percentage(found_skills, job_description):

    if not job_description.strip():

        return 100

    required = []

    jd = job_description.lower()

    for skill in TECH_SKILLS:

        if skill.lower() in jd:

            required.append(skill)

    if len(required) == 0:

        return 100

    matched = 0

    for skill in required:

        if skill in found_skills:

            matched += 1

    percentage = int((matched / len(required)) * 100)

    return percentage
# ==========================================================
# SKILL CATEGORIES
# ==========================================================

SKILL_CATEGORIES = {

    "Programming": [
        "Python", "Java", "C", "C++", "JavaScript"
    ],

    "Database": [
        "SQL", "MySQL", "MongoDB"
    ],

    "Machine Learning": [
        "Machine Learning",
        "Scikit-learn",
        "TensorFlow",
        "Keras"
    ],

    "Data Analysis": [
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Excel"
    ],

    "Visualization": [
        "Power BI",
        "Tableau"
    ],

    "Version Control": [
        "Git",
        "GitHub"
    ]
}

# ==========================================================
# CATEGORIZE SKILLS
# ==========================================================

def categorize_skills(found_skills):

    result = {}

    for category, skills in SKILL_CATEGORIES.items():

        result[category] = []

        for skill in skills:

            if skill in found_skills:

                result[category].append(skill)

    return result


# ==========================================================
# TOP SKILLS
# ==========================================================

def top_skills(found_skills, limit=5):

    return found_skills[:limit]


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def unique_skills(found_skills):

    return sorted(list(set(found_skills)))


# ==========================================================
# CHECK SKILL
# ==========================================================

def has_skill(found_skills, skill):

    return skill in found_skills


# ==========================================================
# SKILL REPORT
# ==========================================================

def skill_report(found_skills, missing_skills):

    return {

        "Detected Skills": found_skills,

        "Missing Skills": missing_skills,

        "Total Skills": len(found_skills),

        "Missing Count": len(missing_skills)

    }


# ==========================================================
# SKILL LEVEL
# ==========================================================

def skill_level(found_skills):

    total = len(found_skills)

    if total >= 15:
        return "Expert"

    elif total >= 10:
        return "Advanced"

    elif total >= 5:
        return "Intermediate"

    else:
        return "Beginner"
