# ==========================================================
# AI RESUME FEEDBACK
# ==========================================================

def generate_summary(
        ats_score,
        found_skills,
        missing_skills
):

    summary = []

    if ats_score >= 85:

        summary.append(
            "Your resume has a strong ATS score."
        )

    elif ats_score >= 60:

        summary.append(
            "Your resume is moderately optimized."
        )

    else:

        summary.append(
            "Your resume needs ATS optimization."
        )

    summary.append(
        f"Detected Skills : {len(found_skills)}"
    )

    summary.append(
        f"Missing Skills : {len(missing_skills)}"
    )

    return summary


# ==========================================================
# RESUME SECTION CHECK
# ==========================================================

def check_resume_sections(resume_text):

    resume = resume_text.lower()

    sections = {

        "Career Objective":[
            "objective",
            "summary",
            "profile"
        ],

        "Education":[
            "education",
            "qualification"
        ],

        "Skills":[
            "skills"
        ],

        "Projects":[
            "project"
        ],

        "Experience":[
            "experience",
            "internship"
        ],

        "Certifications":[
            "certificate",
            "certification"
        ]

    }

    result = {}

    for section, keywords in sections.items():

        found = False

        for keyword in keywords:

            if keyword in resume:

                found = True

                break

        result[section] = found

    return result


# ==========================================================
# COMPLETENESS SCORE
# ==========================================================

def completeness_score(section_result):

    total = len(section_result)

    present = 0

    for value in section_result.values():

        if value:

            present += 1

    return round(
        (present / total) * 100
    )


# ==========================================================
# RESUME STRENGTH
# ==========================================================

def resume_strength(
        ats_score,
        completeness,
        found_skills
):

    strength = (

        ats_score * 0.5

        +

        completeness * 0.3

        +

        len(found_skills) * 2

    )

    return min(round(strength),100)


# ==========================================================
# CAREER RECOMMENDATION
# ==========================================================

def recommend_roles(found_skills):

    roles = []

    skills = [skill.lower() for skill in found_skills]

    if "python" in skills:
        roles.append("Python Developer")

    if "machine learning" in skills:
        roles.append("Machine Learning Engineer")

    if "data science" in skills:
        roles.append("Data Scientist")

    if "sql" in skills:
        roles.append("Data Analyst")

    if "react" in skills:
        roles.append("Frontend Developer")

    if "node.js" in skills or "nodejs" in skills:
        roles.append("Backend Developer")

    if "java" in skills:
        roles.append("Java Developer")

    if "c++" in skills:
        roles.append("Software Engineer")

    if len(roles) == 0:
        roles.append("Software Developer")

    return list(dict.fromkeys(roles))
