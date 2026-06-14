import sqlite3

conn = sqlite3.connect("career.db")
cursor = conn.cursor()

# Delete all ATS records
cursor.execute("DELETE FROM ats_scores")

# Reset auto increment counter
cursor.execute(
    "DELETE FROM sqlite_sequence WHERE name='ats_scores'"
)

conn.commit()
conn.close()

print("Database reset successfully")