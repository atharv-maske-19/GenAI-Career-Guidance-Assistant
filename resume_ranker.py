def rank_resume(
    ats_score,
    readiness_score
):

    final_score = int(
        (ats_score * 0.6) +
        (readiness_score * 0.4)
    )

    return final_score