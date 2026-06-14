from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AQ.Ab8RN6LxaoXijb0_4Dvtfhj_LN0ujQ1PpHrLV5TFwt8LOpys9w")
)

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