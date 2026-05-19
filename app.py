# AI Resume Analyzer & Interview Bot
import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------
# Function to Extract Text from PDF
# ---------------------------------------------------
def extract_text_from_pdf(pdf_file):

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


# ---------------------------------------------------
# Skills List
# ---------------------------------------------------
skills_list = [
    "python",
    "java",
    "machine learning",
    "sql",
    "html",
    "css",
    "javascript",
    "data science",
    "tensorflow",
    "pandas",
    "numpy"
]


# ---------------------------------------------------
# Streamlit UI
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Resume Analyzer & Interview Bot")

st.write(
    "Upload your resume and get ATS score, interview questions and AI feedback."
)

# ---------------------------------------------------
# Upload Resume
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ---------------------------------------------------
# Job Description Input
# ---------------------------------------------------
job_description = st.text_area(
    "Paste Job Description"
)

# ---------------------------------------------------
# Main Logic
# ---------------------------------------------------
if uploaded_file is not None:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # ---------------------------------------------------
    # Resume Text
    # ---------------------------------------------------
    st.subheader("📄 Resume Text")

    st.write(resume_text)

    # ---------------------------------------------------
    # Skill Extraction
    # ---------------------------------------------------
    found_skills = []

    for skill in skills_list:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    # ---------------------------------------------------
    # Show Skills
    # ---------------------------------------------------
    st.subheader("🛠️ Detected Skills")

    if len(found_skills) > 0:

        st.success(", ".join(found_skills))

    else:

        st.warning("No matching skills found.")

    # ---------------------------------------------------
    # ATS Score Calculation
    # ---------------------------------------------------
    if job_description:

        text = [resume_text, job_description]

        cv = CountVectorizer()

        matrix = cv.fit_transform(text)

        similarity = cosine_similarity(matrix)[0][1]

        ats_score = round(similarity * 100, 2)

        # ---------------------------------------------------
        # Show ATS Score
        # ---------------------------------------------------
        st.subheader("📊 ATS Match Score")

        st.success(f"{ats_score}% Match")

        # ATS Feedback
        if ats_score >= 80:

            st.success("Excellent Resume Match ")

        elif ats_score >= 50:

            st.warning("Good Match  Improve some skills.")

        else:

            st.error("Low Match Improve your resume.")

    # ---------------------------------------------------
    # Generate Interview Questions
    # ---------------------------------------------------
    st.subheader("Generated Interview Questions")

    questions = []

    if "python" in found_skills:

        questions.append(
            "Explain OOP concepts in Python."
        )

    if "machine learning" in found_skills:

        questions.append(
            "What is train-test split in Machine Learning?"
        )

    if "sql" in found_skills:

        questions.append(
            "Explain JOINs in SQL."
        )

    if "javascript" in found_skills:

        questions.append(
            "Difference between var, let and const."
        )

    if "java" in found_skills:

        questions.append(
            "Explain inheritance in Java."
        )

    # Default Question
    if len(questions) == 0:

        questions.append(
            "Tell me about yourself."
        )

    # ---------------------------------------------------
    # Correct Keywords for AI Checking
    # ---------------------------------------------------
    correct_answers = {

        "Explain OOP concepts in Python.": [
            "class",
            "object",
            "inheritance",
            "polymorphism",
            "encapsulation"
        ],

        "What is train-test split in Machine Learning?": [
            "training",
            "testing",
            "data",
            "model",
            "split"
        ],

        "Explain JOINs in SQL.": [
            "inner join",
            "left join",
            "right join",
            "table"
        ],

        "Difference between var, let and const.": [
            "scope",
            "block",
            "reassign",
            "javascript"
        ],

        "Explain inheritance in Java.": [
            "parent",
            "child",
            "extends",
            "reuse"
        ]
    }

    # ---------------------------------------------------
    # Show Questions + Take Answers
    # ---------------------------------------------------
    for i, q in enumerate(questions):

        st.write(f"### Question {i+1}")

        st.write(q)

        # ---------------------------------------------------
        # User Answer Input
        # ---------------------------------------------------
        answer = st.text_area(
            f"Your Answer for Question {i+1}",
            key=i
        )

        # ---------------------------------------------------
        # AI Answer Evaluation
        # ---------------------------------------------------
        if answer:

            answer = answer.lower()

            matched_keywords = 0

            # Check Keywords
            if q in correct_answers:

                keywords = correct_answers[q]

                for word in keywords:

                    if word in answer:

                        matched_keywords += 1

                # Accuracy Calculation
                accuracy = (
                    matched_keywords / len(keywords)
                ) * 100

                st.write(
                    f" Accuracy: {round(accuracy, 2)}%"
                )

                # ---------------------------------------------------
                # AI Feedback
                # ---------------------------------------------------
                if accuracy >= 70:

                    st.success(
                        " Correct Answer"
                    )

                elif accuracy >= 40:

                    st.warning(
                        "Partially Correct Answer"
                    )

                else:

                    st.error(
                        " Answer seems Incorrect"
                    )

            else:

                st.info(
                    "No AI evaluation available."
                )

