career_skills = {
    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "machine learning",
        "statistics",
        "pandas",
        "numpy"
    ],

    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch"
    ]
}


def recommend_career(resume_text):

    resume_text = resume_text.lower()

    scores = {}

    for career, skills in career_skills.items():

        score = 0

        for skill in skills:
            if skill in resume_text:
                score += 1

        scores[career] = score

    best_career = max(scores, key=scores.get)

    return best_career, scores


def find_missing_skills(resume_text, career):

    resume_text = resume_text.lower()

    missing = []

    for skill in career_skills[career]:
        if skill not in resume_text:
            missing.append(skill)

    return missing