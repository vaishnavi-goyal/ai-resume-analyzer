from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# ATS SCORE
# ==========================================================

def calculate_ats_score(resume_text, job_description):

    text = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    score = round(similarity * 100, 2)

    return score


# ==========================================================
# ATS RATING
# ==========================================================

def get_resume_rating(score):

    if score >= 90:

        return "⭐⭐⭐⭐⭐", "Excellent Resume"

    elif score >= 75:

        return "⭐⭐⭐⭐", "Very Good Resume"

    elif score >= 60:

        return "⭐⭐⭐", "Good Resume"

    elif score >= 40:

        return "⭐⭐", "Needs Improvement"

    else:

        return "⭐", "Poor Resume"


# ==========================================================
# AI FEEDBACK
# ==========================================================

def get_feedback(score):

    if score >= 90:

        return """
Excellent Resume!

✅ Highly ATS Optimized

✅ Strong keyword matching

✅ Professional formatting

✅ Ready for interviews
"""

    elif score >= 75:

        return """
Very Good Resume

• Add a few more keywords

• Improve project descriptions

• Add measurable achievements
"""

    elif score >= 60:

        return """
Good Resume

• Add technical skills

• Improve summary

• Include certifications
"""

    elif score >= 40:

        return """
Needs Improvement

• Resume is missing keywords

• Add projects

• Improve formatting

• Add experience
"""

    else:

        return """
Poor ATS Score

• Rewrite Resume

• Add Projects

• Add Skills

• Improve ATS Keywords
"""
