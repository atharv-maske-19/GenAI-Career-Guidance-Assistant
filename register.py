from database import conn, cursor

def register_user(
    username,
    password
):

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()