from career_recommender import career_skills

def calculate_score(found_skills, career):

    required = career_skills[career]

    matched = 0

    for skill in required:
        if skill in found_skills:
            matched += 1

    score = int((matched / len(required)) * 100)

    return score