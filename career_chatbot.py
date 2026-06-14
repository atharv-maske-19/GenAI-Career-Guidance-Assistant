from google import genai
import time

client = genai.Client(
    api_key="YOUR_API_KEY"  
)

def get_career_advice(question, resume_text):

    prompt = f"""
You are an expert AI Career Counselor.

Candidate Resume:
{resume_text}

User Question:
{question}

Instructions:
- Answer ONLY the user's question.
- Use resume information when relevant.
- Give specific and practical advice.
- If the question asks for certifications, provide certifications.
- If the question asks for skills, provide skills.
- If the question asks for career roadmap, provide a roadmap.
- Do not give the same generic answer every time.
- Keep the answer under 300 words.
"""

    for _ in range(3):

        try:

            print("QUESTION:", question)

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )

            print("ANSWER:", response.text)

            return response.text

        except Exception as e:

            print("Gemini Error:", e)

            time.sleep(5)

    return "Unable to generate advice right now."