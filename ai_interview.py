from google import genai

client = genai.Client(
    api_key="YOUR_API_KEY"
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