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
from report import create_pdf_report
from gemini_ai import (
    analyze_resume,
    generate_cover_letter,
    rewrite_resume,
    generate_interview_questions,
    company_match,
    career_roadmap
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# LOAD CSS
# ==========================================================

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


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
# HERO SECTION
# ==========================================================

st.markdown(
    """
<div class="hero">

<h1>🤖 AI Resume Analyzer Pro</h1>

<h3>
Smart ATS Checker • AI Resume Review • Mock Interview
</h3>

<p>
Upload your resume, compare it with the job description,
improve your ATS score and get AI-powered career insights.
</p>

</div>
""",
    unsafe_allow_html=True
)


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

    st.success("Company Match")

    st.success("Career Roadmap")

    st.markdown("---")

    st.caption("Developed by Vaishnavi Goyal")

    # ==========================================================
# RESUME UPLOAD
# ==========================================================

st.markdown("---")
st.subheader("📄 Upload Resume")

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(

        "Paste Job Description",

        value=st.session_state.job_description,

        height=250,

        placeholder="""
Example

Python Developer

Skills Required

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

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)


# ==========================================================
# START ANALYSIS
# ==========================================================

if analyze:

    if uploaded_file is None:

        st.warning("⚠ Please upload your resume.")

        st.stop()

    if job_description.strip() == "":

        st.warning("⚠ Please paste Job Description.")

        st.stop()

    resume_text = extract_resume_text(uploaded_file)

    st.session_state.resume_text = resume_text

    st.session_state.job_description = job_description

    st.success("✅ Resume Uploaded Successfully")

    st.markdown("---")

    # ==========================================================
# RESUME STATISTICS
# ==========================================================

stats = get_resume_statistics(
    st.session_state.resume_text
)

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


# ==========================================================
# RESUME PREVIEW
# ==========================================================

st.subheader("📄 Resume Preview")

st.text_area(

    "",

    st.session_state.resume_text[:3000],

    height=250

)

st.markdown("---")


# ==========================================================
# ATS SCORE
# ==========================================================

ats_score = calculate_ats_score(

    st.session_state.resume_text,

    st.session_state.job_description

)

st.session_state.ats_score = ats_score


rating, status = get_resume_rating(
    ats_score
)

feedback = get_feedback(
    ats_score
)


# ==========================================================
# SKILL DETECTION
# ==========================================================

found_skills = detect_skills(

    st.session_state.resume_text

)

missing_skills = get_missing_skills(

    found_skills,

    st.session_state.job_description

)

st.session_state.found_skills = found_skills

st.session_state.missing_skills = missing_skills


# ==========================================================
# AI INSIGHTS
# ==========================================================

summary = generate_summary(

    ats_score,

    found_skills,

    missing_skills

)

sections = check_resume_sections(

    st.session_state.resume_text

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

st.success("✅ Resume Analysis Completed")

st.markdown("---")

# ==========================================================
# ATS DASHBOARD
# ==========================================================

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

st.info(feedback)

st.markdown("---")


# ==========================================================
# CHARTS
# ==========================================================

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

st.markdown("---")


# ==========================================================
# SKILLS ANALYSIS
# ==========================================================

st.subheader("🛠 Skills Analysis")

left, right = st.columns(2)

with left:

    st.success("Detected Skills")

    if found_skills:

        for skill in found_skills:

            st.write(f"✅ {skill}")

    else:

        st.warning("No skills detected.")

with right:

    st.error("Missing Skills")

    if missing_skills:

        for skill in missing_skills:

            st.write(f"❌ {skill}")

    else:

        st.success("No missing skills 🎉")


st.markdown("---")


# ==========================================================
# AI RESUME INSIGHTS
# ==========================================================

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


# ==========================================================
# RESUME SECTIONS
# ==========================================================

st.subheader("📄 Resume Sections")

for section, present in sections.items():

    if present:

        st.success(f"✅ {section}")

    else:

        st.error(f"❌ {section}")


# ==========================================================
# RECOMMENDED ROLES
# ==========================================================

st.markdown("---")

st.subheader("💼 Recommended Job Roles")

for role in roles:

    st.success(role)

st.markdown("---")

# ==========================================================
# PDF REPORT
# ==========================================================

st.subheader("📄 Download Report")

try:


    pdf = create_pdf_report(
        ats_score=ats_score,
        rating=rating,
        found_skills=found_skills,
        missing_skills=missing_skills,
        feedback=feedback,
        strength=strength,
        completeness=complete,
        roles=roles
    )

    st.download_button(
        "📥 Download PDF Report",
        data=pdf,
        file_name="Resume_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

except Exception as e:
    st.error(f"PDF Error: {e}")
except Exception as e:

    st.error(f"PDF Error : {e}")


st.markdown("---")


# ==========================================================
# AI RESUME REVIEW
# ==========================================================

st.subheader("🤖 AI Resume Review")

if st.button(

    "Generate AI Review",

    use_container_width=True

):

    with st.spinner("Analyzing Resume..."):

        review = analyze_resume(

            st.session_state.resume_text,

            st.session_state.job_description

        )

        st.success("Review Generated")

        st.write(review)


st.markdown("---")


# ==========================================================
# AI COVER LETTER
# ==========================================================

st.subheader("📩 AI Cover Letter")

if st.button(

    "Generate Cover Letter",

    use_container_width=True

):

    with st.spinner("Writing Cover Letter..."):

       cover_letter = generate_cover_letter(
       st.session_state.resume_text,
       st.session_state.job_description
)

    st.text_area(

            "Cover Letter",

            cover_letter,

            height=350

        )


st.markdown("---")


# ==========================================================
# AI RESUME REWRITER
# ==========================================================

st.subheader("✨ Resume Rewriter")

if st.button(

    "Rewrite Resume",

    use_container_width=True

):

    with st.spinner("Improving Resume..."):

        rewritten = rewrite_resume(

            st.session_state.resume_text,

            st.session_state.job_description

        )

        st.text_area(

            "Improved Resume",

            rewritten,

            height=450

        )


st.markdown("---")
# ==========================================================
# MOCK INTERVIEW
# ==========================================================

st.subheader("🎤 AI Mock Interview")

if st.button(
    "Start Mock Interview",
    use_container_width=True
):

    with st.spinner("Generating Interview Questions..."):

        try:

            questions = generate_interview_questions(
                st.session_state.resume_text,
                st.session_state.job_description
            )

            st.success("Interview Questions")

            for line in questions.split("\n"):
                if line.strip():
                    st.write(line)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
# ==========================================================
# COMPANY MATCH
# ==========================================================

st.subheader("🏢 Company Match")

if st.button(
    "Find Matching Companies",
    use_container_width=True
):

    with st.spinner("Finding Companies..."):

        try:

            companies = company_match(
                st.session_state.resume_text,
                st.session_state.job_description
            )

            if isinstance(companies, list):

                for company in companies:
                    st.success(company)

            else:
                st.write(companies)

        except Exception as e:
            st.error(e)

st.markdown("---")


# ==========================================================
# CAREER ROADMAP
# ==========================================================

st.subheader("🛣 AI Career Roadmap")

if st.button(
    "Generate Roadmap",
    use_container_width=True
):

    with st.spinner("Generating Career Roadmap..."):

        try:

            roadmap = career_roadmap(
            st.session_state.resume_text,
            st.session_state.job_description
)

            st.write(roadmap)

        except Exception as e:
            st.error(e)

st.markdown("---")


# ==========================================================
# QUICK SUMMARY
# ==========================================================

st.subheader("📌 Final Summary")

st.success(f"ATS Score : {ats_score}%")

st.success(f"Detected Skills : {len(found_skills)}")

st.success(f"Missing Skills : {len(missing_skills)}")

st.success(f"Resume Strength : {strength}/100")


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;padding:20px;">

<h4>🤖 AI Resume Analyzer Pro</h4>

<p>
Developed using
<b>Python</b>,
<b>Streamlit</b>,
<b>Gemini AI</b>,
<b>Plotly</b>
</p>

<p>
Made with ❤️ by
<b>Vaishnavi Goyal</b>
</p>

</div>
""",
    unsafe_allow_html=True
)
