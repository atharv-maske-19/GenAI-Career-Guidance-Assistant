from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # still keep it

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check .env file")

client = genai.Client(api_key=api_key)
def generate_interview_question(career):

    prompt = f"""
    Generate one interview question for {career}.
    Return only the question.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text