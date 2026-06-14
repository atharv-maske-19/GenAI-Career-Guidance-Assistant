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