def calculate_interview_score(feedback):

    score = 60

    if "10" in feedback or "9" in feedback:
        score = 90

    elif "8" in feedback:
        score = 80

    elif "7" in feedback:
        score = 70

    return score