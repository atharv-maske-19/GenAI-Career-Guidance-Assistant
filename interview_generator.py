def generate_interview_questions(career):

    questions = {

        "Data Scientist": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?",
            "Explain bias vs variance.",
            "What is cross validation?",
            "What is feature engineering?"
        ],

        "Data Analyst": [
            "What is SQL JOIN?",
            "Difference between WHERE and HAVING?",
            "What is Power BI?",
            "What is data cleaning?",
            "Explain KPI."
        ],

        "AI Engineer": [
            "What is a Large Language Model?",
            "What is LangChain?",
            "Explain RAG.",
            "Difference between TensorFlow and PyTorch?",
            "What is fine tuning?"
        ]
    }

    return questions.get(
        career,
        ["No questions available."]
    )