import random

# ==========================================================
# QUESTION DATABASE
# ==========================================================

QUESTION_BANK = {

    "Python":[

        "What is OOP in Python?",

        "Difference between List and Tuple?",

        "Explain Decorators.",

        "What is Exception Handling?",

        "Difference between Deep Copy and Shallow Copy?"

    ],

    "Machine Learning":[

        "Explain Train Test Split.",

        "What is Overfitting?",

        "Difference between Regression and Classification?",

        "What is Cross Validation?",

        "Explain Random Forest."

    ],

    "SQL":[

        "Explain JOIN.",

        "Difference between WHERE and HAVING.",

        "Explain Primary Key.",

        "What is Normalization?",

        "Difference between DELETE and TRUNCATE?"

    ],

    "Java":[

        "Explain Inheritance.",

        "What is Polymorphism?",

        "Difference between Interface and Abstract Class?"

    ]

}


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

def generate_questions(skills):

    questions=[]

    for skill in skills:

        if skill in QUESTION_BANK:

            questions.extend(
                QUESTION_BANK[skill]
            )

    random.shuffle(questions)

    return questions[:10]


# ==========================================================
# SCORE
# ==========================================================

def answer_score(answer):

    if len(answer)<30:

        return 20

    elif len(answer)<80:

        return 50

    elif len(answer)<150:

        return 75

    else:

        return 100


# ==========================================================
# PERFORMANCE
# ==========================================================

def interview_result(score):

    if score>=90:

        return "Excellent"

    elif score>=75:

        return "Very Good"

    elif score>=60:

        return "Good"

    elif score>=40:

        return "Average"

    return "Needs Improvement"
