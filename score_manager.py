from database import conn, cursor

def save_ats_score(username, ats_score):

    print("SAVING:", username, ats_score)

    cursor.execute(
        "INSERT INTO ats_scores(username, ats_score) VALUES(?, ?)",
        (username, ats_score)
    )

    conn.commit()

    print("SAVED SUCCESSFULLY")