import sqlite3

conn = sqlite3.connect(
    "career.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ats_scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    ats_score INTEGER
)
""")

conn.commit()