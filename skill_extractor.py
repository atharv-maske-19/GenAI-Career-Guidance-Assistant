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