print("career_utils loaded")
def calculate_ats_score(resume_text):

    keywords = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "pandas",
        "numpy",
        "statistics",
        "data science",
        "data analytics",
        "power bi",
        "tableau",
        "git",
        "github",
        "streamlit",
        "flask",
        "fastapi",
        "mysql",
        "aws",
        "azure",
        "langchain",
        "llm",
        "rag",
        "ollama"
    ]

    resume_text = resume_text.lower()

    found = 0

    detected_keywords = []

    for keyword in keywords:

        if keyword in resume_text:

            found += 1

            detected_keywords.append(keyword)

    score = int((found / len(keywords)) * 100)

    return score, detected_keywords
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "statistics",
    "data analytics",
    "data science",
    "generative ai",
    "llm",
    "langchain"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills
from career_recommender import career_skills

def calculate_score(found_skills, career):

    required = career_skills[career]

    matched = 0

    for skill in required:
        if skill in found_skills:
            matched += 1

    score = int((matched / len(required)) * 100)

    return score
def rank_resume(
    ats_score,
    readiness_score
):

    final_score = int(
        (ats_score * 0.6) +
        (readiness_score * 0.4)
    )

    return final_score
def calculate_skill_gap(skills, missing_skills):

    total_required = len(skills) + len(missing_skills)

    if total_required == 0:
        return 100

    score = int(
        (len(skills) / total_required) * 100
    )

    return score
def predict_placement(
    ats_score,
    readiness_score,
    interview_score,
    skill_gap_score
):

    score = (
        ats_score * 0.30 +
        readiness_score * 0.30 +
        interview_score * 0.25 +
        skill_gap_score * 0.15
    )

    return round(score, 2)
def analyze_resume(skills, ats_score):

    strengths = []
    weaknesses = []

    if ats_score >= 80:
        strengths.append("Strong ATS Score")
    else:
        weaknesses.append("Improve ATS Score")

    if "python" in skills:
        strengths.append("Good Python Skills")
    else:
        weaknesses.append("Learn Python")

    if "sql" in skills:
        strengths.append("Database Knowledge")
    else:
        weaknesses.append("Learn SQL")

    if "machine learning" in skills:
        strengths.append("Machine Learning Knowledge")
    else:
        weaknesses.append("Learn Machine Learning")

    if "statistics" not in skills:
        weaknesses.append("Learn Statistics")

    if "power bi" not in skills:
        weaknesses.append("Learn Power BI")

    if "aws" not in skills:
        weaknesses.append("Learn AWS Cloud")

    if len(skills) >= 8:
        strengths.append("Diverse Technical Skills")
    else:
        weaknesses.append("Add More Technical Skills")

    return strengths, weaknesses