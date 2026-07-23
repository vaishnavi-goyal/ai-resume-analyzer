import streamlit as st
from resume_parser import extract_resume_text, get_resume_statistics
from skills import detect_skills, get_missing_skills
from ats import calculate_ats_score, get_resume_rating, get_feedback
from ai_feedback import (
    generate_summary,
    check_resume_sections,
    completeness_score,
    resume_strength,
    recommend_roles,
)
from charts import ats_gauge, skill_pie, resume_bar
from report import create_pdf_report
from config import APP_NAME, APP_VERSION, AUTHOR

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ==========================================================
# SESSION STATE
# ==========================================================

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0

if "found_skills" not in st.session_state:
    st.session_state.found_skills = []

if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("""
    <div align="center">

    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    width="100">

    <h2 class="sidebar-title">
    Resume Analyzer
    </h2>

    <p class="sidebar-subtitle">
    AI Powered ATS Checker
    </p>

    </div>

    <hr>

    <h3>✨ Features</h3>

    <div class="feature-card">✅ Resume Parsing</div>

    <div class="feature-card">🎯 ATS Score</div>

    <div class="feature-card">💻 Skills Detection</div>

    <div class="feature-card">📌 Missing Skills</div>

    <div class="feature-card">💡 Resume Feedback</div>

    <div class="feature-card">📊 Charts</div>

    <div class="feature-card">📄 PDF Report</div>

    <hr>

    <div class="developer">
        Developed by<br>
        <b>Vaishnavi Goyal</b>
    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown("""
<div class="hero">

<div class="hero-icon">📄</div>

<div>

<div class="hero-title">
AI Resume Analyzer
</div>

<div class="hero-text">
Analyze your resume, calculate ATS score,
detect technical skills, identify missing skills,
and download a professional PDF report.
</div>

</div>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# RESUME UPLOAD
# ==========================================================

left_col, right_col = st.columns([1, 1])

with left_col:

    st.subheader("📤 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

with right_col:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        placeholder="""
Example:

Python
SQL
Machine Learning
Pandas
NumPy
Scikit-learn
Git
Communication Skills
        """
    )

    st.session_state.job_description = job_description

st.write("---")

# ==========================================================
# RESUME PARSING
# ==========================================================

if uploaded_resume is not None:

    with st.spinner("📄 Reading Resume..."):

        resume_text = extract_resume_text(uploaded_resume)

        st.session_state.resume_text = resume_text

    st.success("✅ Resume Uploaded Successfully")

else:

    st.info("👆 Please upload your resume to continue.")

# ==========================================================
# RESUME STATISTICS
# ==========================================================

if st.session_state.resume_text:

    stats = get_resume_statistics(
        st.session_state.resume_text
    )

    st.subheader("📊 Resume Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📄 Pages",
            stats["pages"]
        )

    with c2:
        st.metric(
            "📝 Words",
            stats["words"]
        )

    with c3:
        st.metric(
            "🔤 Characters",
            stats["characters"]
        )

    with c4:

        reading_time = max(
            1,
            round(stats["words"] / 200)
        )

        st.metric(
            "⏱ Reading Time",
            f"{reading_time} min"
        )

# ==========================================================
# RESUME PREVIEW
# ==========================================================

if st.session_state.resume_text:

    st.write("---")

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        value=st.session_state.resume_text,
        height=350
    )

st.write("---")
# ==========================================================
# SKILLS DETECTION
# ==========================================================

if st.session_state.resume_text:

    st.subheader("🛠 Skills Analysis")

    found_skills = detect_skills(
        st.session_state.resume_text
    )

    missing_skills = get_missing_skills(
        found_skills,
        st.session_state.job_description
    )

    st.session_state.found_skills = found_skills
    st.session_state.missing_skills = missing_skills

    left, right = st.columns(2)

    # ======================================================
    # DETECTED SKILLS
    # ======================================================

    with left:

        st.success("✅ Detected Skills")

        if found_skills:

            for skill in found_skills:
                st.write(f"✔ {skill}")

        else:

            st.warning("No skills detected.")

    # ======================================================
    # MISSING SKILLS
    # ======================================================

    with right:

        st.error("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"✖ {skill}")

        else:

            st.success("No Missing Skills 🎉")

st.write("---")

# ==========================================================
# ATS SCORE
# ==========================================================

if st.session_state.resume_text:

    ats_score = calculate_ats_score(

        st.session_state.resume_text,

        st.session_state.job_description

    )

    st.session_state.ats_score = ats_score

    rating = get_resume_rating(ats_score)

    feedback = get_feedback(ats_score)

    st.subheader("🎯 ATS Score")

    col1, col2 = st.columns([1,1])

    with col1:

        st.metric(

            "ATS Score",

            f"{ats_score}%"

        )

        st.metric(

            "Resume Rating",

            rating

        )

    with col2:

        st.progress(

            ats_score / 100

        )

        st.caption(

            f"Current ATS Score : {ats_score}%"

        )

st.write("---")

# ==========================================================
# ATS FEEDBACK
# ==========================================================

if st.session_state.resume_text:

    st.subheader("💡 ATS Feedback")

    if feedback:

        for item in feedback:

            st.info(item)

    else:

        st.success("Excellent Resume 🎉")
        # ==========================================================
# RESUME ANALYSIS
# ==========================================================

if st.session_state.resume_text:

    st.write("---")

    st.subheader("📋 Resume Analysis")

    summary = generate_summary(
        st.session_state.resume_text
    )

    strength = resume_strength(
        st.session_state.resume_text
    )

    completeness = completeness_score(
        st.session_state.resume_text
    )

    roles = recommend_roles(
        st.session_state.found_skills
    )

    c1, c2 = st.columns(2)

    with c1:

        st.info(summary)

    with c2:

        st.success(f"💪 Resume Strength : {strength}")

        st.metric(
            "📊 Resume Completeness",
            f"{completeness}%"
        )

st.write("---")

# ==========================================================
# RECOMMENDED JOB ROLES
# ==========================================================

if st.session_state.resume_text:

    st.subheader("🎯 Recommended Job Roles")

    if roles:

        cols = st.columns(3)

        for i, role in enumerate(roles):

            with cols[i % 3]:

                st.success(role)

st.write("---")

# ==========================================================
# VISUAL ANALYTICS
# ==========================================================

if st.session_state.resume_text:

    st.subheader("📈 Visual Analytics")

    c1, c2 = st.columns(2)

    with c1:

        fig1 = ats_gauge(
            st.session_state.ats_score
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with c2:

        fig2 = skill_pie(
            len(st.session_state.found_skills),
            len(st.session_state.missing_skills)
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.write("")

    fig3 = resume_bar(
        st.session_state.ats_score,
        completeness
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.write("---")

# ==========================================================
# RESUME CHECKLIST
# ==========================================================

if st.session_state.resume_text:

    st.subheader("✅ Resume Checklist")

    sections = check_resume_sections(
        st.session_state.resume_text
    )

    for section, status in sections.items():

        if status:

            st.success(f"✔ {section}")

        else:

            st.error(f"✖ {section}")
            # ==========================================================
# PDF REPORT DOWNLOAD
# ==========================================================

if st.session_state.resume_text:

    st.write("---")

    st.subheader("📄 Download Resume Report")

    pdf_file = create_pdf_report(
        resume_text=st.session_state.resume_text,
        ats_score=st.session_state.ats_score,
        skills=st.session_state.found_skills,
        missing_skills=st.session_state.missing_skills,
        feedback=feedback
    )

    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_file,
        file_name="Resume_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.write("---")

# ==========================================================
# FINAL RESULT
# ==========================================================

if st.session_state.resume_text:

    if st.session_state.ats_score >= 85:

        st.success(
            "🎉 Excellent Resume! Your resume is highly ATS friendly."
        )

    elif st.session_state.ats_score >= 70:

        st.warning(
            "👍 Good Resume! A few improvements can increase your ATS score."
        )

    else:

        st.error(
            "⚠ Your resume needs improvement. Follow the feedback above."
        )

st.write("---")

# ==========================================================
# QUICK TIPS
# ==========================================================

with st.expander("💡 Resume Tips"):

    st.markdown("""
- Keep resume to **1-2 pages**
- Use ATS-friendly fonts
- Add measurable achievements
- Mention technical skills
- Include projects
- Add certifications
- Keep formatting simple
- Use keywords from the Job Description
- Add GitHub & LinkedIn links
- Proofread before applying
""")

st.write("---")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<div style="text-align:center;padding:20px;">
<h4>📄 AI Resume Analyzer</h4>
<p>Analyze • Improve • Get Hired 🚀</p>
<p>Version : 1.0.0</p>
<p>Developed by Vaishnavi Goyal</p>
</div>
""",
unsafe_allow_html=True
)
# ==========================================================
# RESET ANALYZER
# ==========================================================

st.write("---")

if st.button("🔄 Reset Analyzer", use_container_width=True):

    st.session_state.resume_text = ""
    st.session_state.job_description = ""
    st.session_state.ats_score = 0
    st.session_state.found_skills = []
    st.session_state.missing_skills = []

    st.success("Analyzer reset successfully.")
    st.rerun()

# ==========================================================
# ABOUT
# ==========================================================

with st.expander("ℹ️ About AI Resume Analyzer"):

    st.markdown("""
### 📄 AI Resume Analyzer

This application helps you:

- ✅ Parse Resume PDF
- ✅ Calculate ATS Score
- ✅ Detect Technical Skills
- ✅ Find Missing Skills
- ✅ Generate Resume Feedback
- ✅ Visualize Results
- ✅ Download PDF Report

Developed using:

- Python
- Streamlit
- Plotly
- PyPDF2
- ReportLab
""")

# ==========================================================
# CONTACT
# ==========================================================

with st.expander("📧 Contact"):

    st.write("Developer: **Vaishnavi Goyal**")
    st.write("Project: **AI Resume Analyzer**")
