def generate_roadmap(career, missing_skills):

    roadmap = []

    if career == "Data Scientist":

        roadmap = [
            "Month 1: Python + SQL",
            "Month 2: Statistics + Pandas",
            "Month 3: NumPy + Data Visualization",
            "Month 4: Machine Learning",
            "Month 5: Deep Learning",
            "Month 6: Build Data Science Projects"
        ]

    elif career == "AI Engineer":

        roadmap = [
            "Month 1: Python",
            "Month 2: Machine Learning",
            "Month 3: Deep Learning",
            "Month 4: NLP",
            "Month 5: LLMs + LangChain",
            "Month 6: GenAI Projects"
        ]

    elif career == "Data Analyst":

        roadmap = [
            "Month 1: Excel + SQL",
            "Month 2: Power BI",
            "Month 3: Statistics",
            "Month 4: Python",
            "Month 5: Dashboard Projects",
            "Month 6: Portfolio Building"
        ]

    return roadmap