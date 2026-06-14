def calculate_skill_gap(skills, missing_skills):

    total_required = len(skills) + len(missing_skills)

    if total_required == 0:
        return 100

    score = int(
        (len(skills) / total_required) * 100
    )

    return score