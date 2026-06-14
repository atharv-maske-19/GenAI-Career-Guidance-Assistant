import json
import os

FILE = "interview_history.json"


def save_interview(username, question, answer, feedback):

    data = {
        "user": username,
        "Question": question,
        "Answer": answer,
        "Feedback": feedback
    }

    history = []

    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                history = json.load(f)
        except:
            history = []

    history.append(data)

    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)


def get_history(username):

    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
                return [h for h in data if h.get("user") == username]
        except:
            return []

    return []