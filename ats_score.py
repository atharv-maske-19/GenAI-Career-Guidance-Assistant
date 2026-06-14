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