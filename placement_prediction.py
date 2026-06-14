def predict_placement(
    ats_score,
    readiness_score,
    interview_score,
    skill_gap_score
):

    score = (
        ats_score * 0.30 +
        readiness_score * 0.30 +
        interview_score * 0.25 +
        skill_gap_score * 0.15
    )

    return round(score, 2)