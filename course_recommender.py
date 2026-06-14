def recommend_courses(career):

    courses = {

        "Data Scientist": [
            "Google Data Analytics Professional Certificate",
            "IBM Data Science Professional Certificate",
            "Machine Learning - Andrew Ng",
            "Deep Learning Specialization",
            "Statistics for Data Science"
        ],

        "AI Engineer": [
            "Machine Learning - Andrew Ng",
            "Deep Learning Specialization",
            "Generative AI with LLMs",
            "LangChain for LLM Applications",
            "Google AI Essentials"
        ],

        "Data Analyst": [
            "Google Data Analytics",
            "Excel for Data Analysis",
            "Power BI Complete Course",
            "SQL for Data Analytics",
            "Tableau for Beginners"
        ]
    }

    return courses.get(career, [])