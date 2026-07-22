"""
config.py
------------------------------------
Project Configuration
"""

# ==========================================================
# APP DETAILS
# ==========================================================

APP_NAME = "AI Resume Analyzer"

APP_VERSION = "1.0.0"

AUTHOR = "Vaishnavi Goyal"

# ==========================================================
# SUPPORTED FILE TYPES
# ==========================================================

ALLOWED_FILE_TYPES = ["pdf"]

MAX_FILE_SIZE_MB = 5

# ==========================================================
# ATS SETTINGS
# ==========================================================

MAX_ATS_SCORE = 100

PASSING_SCORE = 70

# ==========================================================
# DEFAULT TECHNICAL SKILLS
# ==========================================================

TECH_SKILLS = [

    "Python",
    "SQL",
    "Excel",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Keras",
    "Power BI",
    "Tableau",
    "Git",
    "GitHub",
    "Streamlit",
    "Flask",
    "Django",
    "HTML",
    "CSS",
    "JavaScript",
    "C",
    "C++",
    "Java"

]

# ==========================================================
# COLORS
# ==========================================================

PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#22C55E"

WARNING_COLOR = "#FACC15"

DANGER_COLOR = "#EF4444"

BACKGROUND_COLOR = "#F8FAFC"

# ==========================================================
# PDF REPORT
# ==========================================================

REPORT_TITLE = "Resume Analysis Report"

REPORT_AUTHOR = AUTHOR
