def match_resume_with_jd(
    resume_text,
    job_description
):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_words = set(
        resume_text.split()
    )

    jd_words = set(
        job_description.split()
    )

    matched = resume_words.intersection(
        jd_words
    )

    score = int(
        (len(matched) / len(jd_words)) * 100
    ) if len(jd_words) > 0 else 0

    missing = jd_words - resume_words

    return (
        score,
        list(matched),
        list(missing)
    )