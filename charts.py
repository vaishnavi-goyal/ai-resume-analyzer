"""
charts.py
---------------------------------
Professional Charts
Using Plotly
"""

import plotly.graph_objects as go
import plotly.express as px

# ==========================================================
# ATS GAUGE CHART
# ==========================================================

def ats_gauge(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "ATS Score"
            },

            number={
                "suffix": "%"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#2563eb"
                },

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#ef4444"
                    },

                    {
                        "range": [40, 70],
                        "color": "#facc15"
                    },

                    {
                        "range": [70, 100],
                        "color": "#22c55e"
                    }

                ]
            }

        )

    )

    fig.update_layout(

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    return fig


# ==========================================================
# SKILL PIE CHART
# ==========================================================

def skill_pie(found, missing):

    labels = [

        "Detected Skills",

        "Missing Skills"

    ]

    values = [

        found,

        missing

    ]

    fig = px.pie(

        names=labels,

        values=values,

        hole=0.45,

        title="Skills Distribution"

    )

    fig.update_layout(

        height=350

    )

    return fig
# ==========================================================
# RESUME SCORE BAR CHART
# ==========================================================

def resume_bar(ats_score, completeness):

    categories = [
        "ATS Score",
        "Completeness"
    ]

    scores = [
        ats_score,
        completeness
    ]

    fig = px.bar(

        x=categories,

        y=scores,

        text=scores,

        title="Resume Performance",

    )

    fig.update_traces(

        textposition="outside"

    )

    fig.update_layout(

        height=400,

        xaxis_title="",

        yaxis_title="Score",

        yaxis_range=[0, 100]

    )

    return fig


# ==========================================================
# SKILLS BAR CHART
# ==========================================================

def skills_bar(found_skills):

    skills = found_skills

    counts = [1] * len(skills)

    fig = px.bar(

        x=skills,

        y=counts,

        text=counts,

        title="Detected Skills"

    )

    fig.update_layout(

        height=400,

        xaxis_title="Skills",

        yaxis_title="Count"

    )

    return fig


# ==========================================================
# KEYWORD MATCH CHART
# ==========================================================

def keyword_match_chart(found, missing):

    labels = [

        "Matched",

        "Missing"

    ]

    values = [

        found,

        missing

    ]

    fig = px.bar(

        x=labels,

        y=values,

        text=values,

        title="Keyword Match"

    )

    fig.update_layout(

        height=350,

        xaxis_title="",

        yaxis_title="Keywords"

    )

    return fig
# ==========================================================
# RESUME STRENGTH CHART
# ==========================================================

def resume_strength_chart(strength):

    levels = {
        "Weak": 25,
        "Average": 50,
        "Good": 75,
        "Excellent": 100
    }

    value = levels.get(strength, 0)

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Resume Strength"],

            y=[value],

            text=[strength],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Resume Strength",

        yaxis=dict(
            range=[0, 100]
        ),

        height=350

    )

    return fig


# ==========================================================
# SECTION SCORE CHART
# ==========================================================

def section_score_chart(section_scores):

    sections = list(section_scores.keys())

    scores = list(section_scores.values())

    fig = px.bar(

        x=sections,

        y=scores,

        text=scores,

        title="Resume Section Scores"

    )

    fig.update_traces(

        textposition="outside"

    )

    fig.update_layout(

        height=400,

        yaxis_range=[0, 100],

        xaxis_title="",

        yaxis_title="Score"

    )

    return fig


# ==========================================================
# DASHBOARD SUMMARY CHART
# ==========================================================

def dashboard_summary_chart(

    ats_score,

    completeness,

    skills_found,

    skills_missing

):

    labels = [

        "ATS Score",

        "Completeness",

        "Skills Found",

        "Skills Missing"

    ]

    values = [

        ats_score,

        completeness,

        skills_found,

        skills_missing

    ]

    fig = px.bar(

        x=labels,

        y=values,

        text=values,

        title="Resume Dashboard"

    )

    fig.update_layout(

        height=400,

        xaxis_title="",

        yaxis_title="Value"

    )

    return fig


# ==========================================================
# EMPTY CHART
# ==========================================================

def empty_chart(message="No Data Available"):

    fig = go.Figure()

    fig.add_annotation(

        text=message,

        showarrow=False,

        font=dict(size=20)

    )

    fig.update_xaxes(

        visible=False

    )

    fig.update_yaxes(

        visible=False

    )

    fig.update_layout(

        height=300,

        title="Information"

    )

    return fig
