import streamlit as st
from config import *
from resume_parser import *
from skills import *
from ats import *
from charts import *
from ai_feedback import *
from report import *
from interview import *
from gemini_ai import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load CSS
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    if "resume_text" not in st.session_state: st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0

if "found_skills" not in st.session_state:
    st.session_state.found_skills = []

if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []
    st.markdown("""
<div class="hero">
<h1>🤖 AI Resume Analyzer Pro</h1>
<h3>Smart ATS Checker • AI Resume Review • Mock Interview</h3>
<p>
Upload your resume, compare it with the job description,
improve your ATS score and get AI-powered career insights.
</p>
</div>
""", unsafe_allow_html=True)
    st.write("✅ Hero ke baad code chal raha hai")
