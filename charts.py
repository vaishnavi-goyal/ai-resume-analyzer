import plotly.graph_objects as go
import plotly.express as px


# ==========================================================
# ATS Gauge Chart
# ==========================================================

def ats_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        number={"suffix":"%"},

        title={"text":"ATS Match Score"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"royalblue"},

            "steps":[

                {"range":[0,40],"color":"#FECACA"},

                {"range":[40,70],"color":"#FDE68A"},

                {"range":[70,100],"color":"#BBF7D0"}

            ]

        }

    ))

    fig.update_layout(height=350)

    return fig


# ==========================================================
# Skills Pie Chart
# ==========================================================

def skill_pie(found, missing):

    if found == 0 and missing == 0:
        found = 1
        missing = 0

    fig = px.pie(
        names=["Matched Skills", "Missing Skills"],
        values=[found, missing],
        hole=0.55
    )

    fig.update_layout(height=350)

    return fig

# ==========================================================
# Resume Statistics
# ==========================================================

def resume_bar(words, chars, skills):

    fig = px.bar(

        x=["Words","Characters","Skills"],

        y=[words, chars, skills],

        text=[words, chars, skills]

    )

    fig.update_layout(height=350)

    return fig
