from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # still keep it

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check .env file")

client = genai.Client(api_key=api_key)
def evaluate_answer(question, answer):

    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Give:
    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improvements
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text