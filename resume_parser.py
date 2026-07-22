"""
resume_parser.py
------------------------------------
Resume PDF Parser
"""

import PyPDF2

# ==========================================================
# EXTRACT TEXT FROM PDF
# ==========================================================

def extract_resume_text(uploaded_file):

    text = ""

    try:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    except Exception:

        return ""

    return text.strip()


# ==========================================================
# RESUME STATISTICS
# ==========================================================

def get_resume_statistics(resume_text):

    words = resume_text.split()

    characters = len(resume_text)

    paragraphs = len(

        [line for line in resume_text.split("\n") if line.strip()]

    )

    return {

        "pages": max(1, paragraphs // 40 + 1),

        "words": len(words),

        "characters": characters,

        "paragraphs": paragraphs

    }


# ==========================================================
# GET EMAIL
# ==========================================================

def get_email(resume_text):

    import re

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, resume_text)

    if match:

        return match.group()

    return "Not Found"


# ==========================================================
# GET PHONE
# ==========================================================

def get_phone(resume_text):

    import re

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, resume_text)

    if match:

        return match.group()

    return "Not Found"
# ==========================================================
# GET NAME
# ==========================================================

def get_name(resume_text):

    lines = resume_text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2 and len(line) < 40:

            if not any(char.isdigit() for char in line):

                return line

    return "Not Found"


# ==========================================================
# GET LINKS
# ==========================================================

def get_links(resume_text):

    import re

    pattern = r"https?://[^\s]+"

    return re.findall(pattern, resume_text)


# ==========================================================
# CLEAN RESUME TEXT
# ==========================================================

def clean_resume_text(resume_text):

    import re

    text = resume_text.lower()

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    return text.strip()


# ==========================================================
# EXTRACT SECTIONS
# ==========================================================

def extract_sections(resume_text):

    sections = {

        "Summary": False,
        "Education": False,
        "Skills": False,
        "Projects": False,
        "Experience": False,
        "Certifications": False

    }

    text = resume_text.lower()

    if "summary" in text or "objective" in text:
        sections["Summary"] = True

    if "education" in text:
        sections["Education"] = True

    if "skills" in text:
        sections["Skills"] = True

    if "project" in text:
        sections["Projects"] = True

    if "experience" in text or "internship" in text:
        sections["Experience"] = True

    if "certification" in text or "certificate" in text:
        sections["Certifications"] = True

    return sections


# ==========================================================
# RESUME SUMMARY
# ==========================================================

def get_resume_summary(resume_text):

    words = resume_text.split()

    if len(words) <= 50:

        return resume_text

    return " ".join(words[:50]) + "..."
