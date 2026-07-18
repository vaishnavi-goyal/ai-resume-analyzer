# ==========================================================
# IMPORTS
# ==========================================================

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

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#EEF5FF,#F8FAFC);
}

/* Hide Streamlit Menu */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Hero */

.hero{
    background:linear-gradient(135deg,#0F172A,#2563EB);
    padding:40px;
    border-radius:20px;
    text-align:center;
    margin-bottom:30px;
    box-shadow:0px 10px 25px rgba(0,0,0,.2);
}

.hero h1{
    color:#111827 !important;
    font-size:42px;
    margin:0;
    font-weight:700;
}

.hero h3{
    color:#E2E8F0 !important;
    margin-top:10px;
}

h2{
color:#111827 !important;
}
            
.hero p{
    color:white !important;
    font-size:18px;
}

/* Upload Box */

[data-testid="stFileUploader"]{
    background:white;
    border:2px dashed #2563EB;
    border-radius:15px;
    padding:15px;
}

/* Upload Area */

[data-testid="stFileUploaderDropzone"]{
    background:#F8FAFC !important;
    border:2px dashed #3B82F6 !important;
    border-radius:15px !important;
}

/* Upload Button */

[data-testid="stFileUploader"] button{
    background:#2563EB !important;
    color:white !important;
    border-radius:10px !important;
    border:none !important;
}

/* Upload Text */

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p{
    color:#475569 !important;
    font-size:15px !important;
}

/* Remove Dark Background */

[data-testid="stFileUploaderDropzone"] > div{
    background:#F8FAFC !important;
}

/* Upload Text */

[data-testid="stFileUploader"] *{
    color:#111827 !important;
}

/* Text Area */

textarea{
    background:white !important;
    color:#111827 !important;
    border:2px solid #2563EB !important;
    border-radius:12px !important;
}

/* Labels */

label{
    color:#111827 !important;
    font-weight:bold;
}

/* Button */

.stButton>button{
    width:100%;
    height:50px;
    background:#2563EB;
    color:white;
    font-size:18px;
    border:none;
    border-radius:12px;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Metrics */

[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}
# /* ===========================
#    HEADINGS
# =========================== */

h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

# /* ===========================
#    Metric Label
# =========================== */

[data-testid="stMetricLabel"]{
    color:#111827 !important;
    font-weight:600;
}

# /* ===========================
#    Metric Value
# =========================== */

[data-testid="stMetricValue"]{
    color:#111827 !important;
    font-size:34px !important;
    font-weight:bold;
}

# /* ===========================
#    Metric Card
# =========================== */

[data-testid="metric-container"]{
    background:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
}

# /* ===========================
#    Text Area
# =========================== */

textarea{
    color:#111827 !important;
}
# /* ===========================
#    Resume Preview
# =========================== */

[data-testid="stTextArea"] label{
    color:#111827 !important;
    font-weight:bold;
}

/* ===========================
   GLOBAL TEXT COLOR
=========================== */

html,
body,
div,
span,
p,
label,
small,
strong,
b,
li{
    color:#111827 !important;
}

/* ===========================
   ALL HEADINGS
=========================== */

h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

/* ===========================
   Streamlit Markdown
=========================== */

.stMarkdown,
.stMarkdown p,
.stMarkdown div{
    color:#111827 !important;
}

/* ===========================
   Streamlit Text
=========================== */

.stText{
    color:#111827 !important;
}

/* ===========================
   Metric
=========================== */

[data-testid="stMetricLabel"]{
    color:#111827 !important;
}

[data-testid="stMetricValue"]{
    color:#111827 !important;
    font-weight:bold;
}

/* ===========================
   Success / Info / Error
=========================== */

.stSuccess{
    color:#111827 !important;
}

.stInfo{
    color:#111827 !important;
}

.stWarning{
    color:#111827 !important;
}

.stError{
    color:#111827 !important;
}

/* ===========================
   Progress Text
=========================== */

.stProgress{
    color:#111827 !important;
}

/* ===========================
   Buttons
=========================== */

button{
    color:white !important;
}

/* ===========================
   TextArea
=========================== */

textarea{
    color:#111827 !important;
}

/* ===========================
   Download Button
=========================== */

[data-testid="stDownloadButton"] *{
    color:white !important;
}

/* ===========================
   Write()
=========================== */

[data-testid="stMarkdownContainer"]{
    color:#111827 !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">

<h1>🤖 AI Resume Analyzer Pro</h1>

<h3>Smart ATS Checker • AI Resume Review • Mock Interview</h3>

<p>
Upload your resume, compare it with the job description,
improve your ATS score, and get AI-powered career insights.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📌 Dashboard")

    st.success("ATS Resume Analysis")

    st.success("Skill Detection")

    st.success("AI Resume Review")

    st.success("PDF Report")

    st.success("Mock Interview")

    st.markdown("---")

    st.info("Version 2.0")

    st.caption("Developed by Vaishnavi Goyal")

    # ==========================================================
# RESUME UPLOAD
# ==========================================================

st.markdown("## 📄 Upload Resume")

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(

        "Paste Job Description",

        height=250,

        placeholder="""
Example:

Python Developer

Skills Required:

Python
SQL
Machine Learning
Pandas
NumPy
Git
Communication

"""
    )

# ==========================================================
# ANALYZE BUTTON
# ==========================================================

analyze = st.button("🚀 Analyze Resume")

# ==========================================================
# START ANALYSIS
# ==========================================================

if analyze:

    if uploaded_file is None:

        st.warning("⚠ Please upload your Resume.")

        st.stop()

    if job_description.strip() == "":

        st.warning("⚠ Please paste Job Description.")

        st.stop()

    # ======================================================
    # EXTRACT RESUME
    # ======================================================

    resume_text = extract_resume_text(
        uploaded_file
    )

    stats = get_resume_statistics(
        resume_text
    )

    st.success("✅ Resume Uploaded Successfully")

    st.markdown("---")

    # ======================================================
    # RESUME STATISTICS
    # ======================================================

    st.subheader("📊 Resume Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Words",

            stats["words"]

        )

    with c2:

        st.metric(

            "Characters",

            stats["characters"]

        )

    with c3:

        st.metric(

            "Lines",

            stats["lines"]

        )

    st.markdown("---")

    st.subheader("📄 Resume Preview")

    st.text_area(

        "",

        resume_text[:3000],

        height=250

    )

    # ======================================================
    # ATS SCORE
    # ======================================================

    ats_score = calculate_ats_score(

        resume_text,

        job_description

    )

    rating, status = get_resume_rating(

        ats_score

    )

    feedback = get_feedback(

        ats_score

    )
        # ======================================================
    # SKILL DETECTION
    # ======================================================

    found_skills = detect_skills(
        resume_text
    )

    missing_skills = get_missing_skills(
        found_skills,
        job_description
    )

    # ======================================================
    # AI RESUME ANALYSIS
    # ======================================================

    summary = generate_summary(
        ats_score,
        found_skills,
        missing_skills
    )

    sections = check_resume_sections(
        resume_text
    )

    complete = completeness_score(
        sections
    )

    strength = resume_strength(
        ats_score,
        complete,
        found_skills
    )

    roles = recommend_roles(
        found_skills
    )

    # ======================================================
    # ATS DASHBOARD
    # ======================================================

    st.markdown("---")

    st.subheader("📊 ATS Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

    with c2:

        st.metric(
            "Rating",
            rating
        )

    with c3:

        st.metric(
            "Status",
            status
        )

    # ======================================================
    # CHARTS
    # ======================================================

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            ats_gauge(
                ats_score
            ),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            skill_pie(

                len(found_skills),

                len(missing_skills)

            ),

            use_container_width=True

        )

    st.plotly_chart(

        resume_bar(

            stats["words"],

            stats["characters"],

            len(found_skills)

        ),

        use_container_width=True

    )

    # ======================================================
    # SKILLS
    # ======================================================

    st.markdown("---")

    st.subheader("🛠 Skills Analysis")

    left, right = st.columns(2)

    with left:

        st.success("Detected Skills")

        if found_skills:

            for skill in found_skills:

                st.write("✅", skill)

        else:

            st.warning("No Skills Found")

    with right:

        st.error("Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.write("❌", skill)

        else:

            st.success("No Missing Skills 🎉")
                # ======================================================
    # AI RESUME INSIGHTS
    # ======================================================

    st.markdown("---")

    st.subheader("🤖 AI Resume Insights")

    for line in summary:

        st.info(line)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Resume Completeness",
            f"{complete}%"
        )

    with c2:

        st.metric(
            "Resume Strength",
            f"{strength}/100"
        )

    st.markdown("---")

    st.subheader("📄 Resume Sections")

    for section, present in sections.items():

        if present:

            st.success(f"✅ {section}")

        else:

            st.error(f"❌ {section}")

    # ======================================================
    # CAREER RECOMMENDATIONS
    # ======================================================

    st.markdown("---")

    st.subheader("💼 Recommended Job Roles")

    for role in roles:

        st.success(role)

    # ======================================================
    # PDF REPORT
    # ======================================================

    create_pdf_report(

        "resume_report.pdf",

        ats_score,

        rating,

        found_skills,

        missing_skills,

        feedback,

        strength,

        complete,

        roles

    )

    with open("resume_report.pdf", "rb") as pdf:

        st.download_button(

            label="📥 Download Resume Report",

            data=pdf,

            file_name="AI_Resume_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    # ======================================================
    # GEMINI AI REVIEW
    # ======================================================

    st.markdown("---")

    st.subheader("🤖 Gemini AI Resume Review")

    if st.button("✨ Generate AI Review"):

        with st.spinner("Gemini AI is reviewing your resume..."):

            try:

                review = analyze_resume(

                    resume_text,

                    job_description

                )

                st.success("Analysis Completed")

                st.markdown(review)

            except Exception as e:

                st.error(f"Gemini Error: {e}")

    # ======================================================
    # INTERVIEW
    # ======================================================

    st.markdown("---")

    st.subheader("🎤 AI Mock Interview")

    questions = generate_questions(
        found_skills
    )

    if questions:

        total = 0

        for i, question in enumerate(questions):

            st.write(f"### Question {i+1}")

            st.info(question)

            answer = st.text_area(

                "Your Answer",

                key=f"answer_{i}"

            )

            if answer:

                score = answer_score(answer)

                total += score

                st.progress(score/100)

                st.write(f"Score : {score}/100")

        final_score = total // len(questions)

        st.markdown("---")

        st.metric(

            "Interview Score",

            f"{final_score}/100"

        )

        st.success(

            interview_result(final_score)

        )
            # ======================================================
    # COMPANY RESUME MATCH
    # ======================================================

    st.markdown("---")
    st.subheader("🏢 Company Resume Match")

    companies = {
        "Google": ["Python", "Machine Learning", "SQL", "Git"],
        "Microsoft": ["Python", "Azure", "SQL", "C++"],
        "Amazon": ["Python", "DSA", "SQL", "AWS"],
        "TCS": ["Java", "SQL", "Communication"],
        "Infosys": ["Python", "SQL", "Problem Solving"]
    }

    for company, required in companies.items():

        matched = len(
            set(found_skills).intersection(required)
        )

        score = int((matched / len(required)) * 100)

        st.write(f"### {company}")

        st.progress(score / 100)

        st.write(f"Match Score : {score}%")

    # ======================================================
    # CAREER ROADMAP
    # ======================================================

    st.markdown("---")
    st.subheader("🎯 Career Roadmap")

    if ats_score >= 80:

        st.success("""
✅ Resume is strong.

Next Steps

• Apply for internships

• Practice DSA

• Build ML Projects

• Prepare Interview Questions

• Keep Updating Resume
""")

    elif ats_score >= 60:

        st.warning("""
Improve Resume

• Add Projects

• Add Certifications

• Improve Skills

• Optimize Resume Keywords

• Practice Aptitude
""")

    else:

        st.error("""
Resume Needs Improvement

• Learn Python

• Learn SQL

• Build Projects

• Add Technical Skills

• Improve ATS Score
""")

    # ======================================================
    # AI COVER LETTER
    # ======================================================

    st.markdown("---")
    st.subheader("📧 AI Cover Letter")

    if st.button("Generate Cover Letter"):

        prompt = f"""
Write a professional cover letter.

Resume

{resume_text}

Job Description

{job_description}
"""

        with st.spinner("Generating Cover Letter..."):

            try:

                cover = analyze_resume(
                    prompt,
                    ""
                )

                st.markdown(cover)

            except Exception as e:

                st.error(e)

    # ======================================================
    # AI RESUME REWRITER
    # ======================================================

    st.markdown("---")
    st.subheader("✨ AI Resume Rewriter")

    if st.button("Rewrite Resume"):

        prompt = f"""
Rewrite this resume professionally.

Resume

{resume_text}
"""

        with st.spinner("Improving Resume..."):

            try:

                improved = analyze_resume(
                    prompt,
                    ""
                )

                st.markdown(improved)

            except Exception as e:

                st.error(e)

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown("---")

    st.caption(
        "🤖 AI Resume Analyzer Pro | Developed by Vaishnavi Goyal"
    )


