from config import TECH_SKILLS


def detect_skills(resume_text):

    detected = []

    resume = resume_text.lower()

    for skill in TECH_SKILLS:

        if skill.lower() in resume:

            detected.append(skill)

    return detected


def get_missing_skills(resume_skills, job_description):

    missing = []

    jd = job_description.lower()

    for skill in TECH_SKILLS:

        if skill.lower() in jd:

            if skill not in resume_skills:

                missing.append(skill)

    return missing