from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_mcqs(text):

    prompt = f"""
    Generate exactly 5 multiple choice questions from the content below.

    Return ONLY valid JSON.

    Example format:

    [
      {{
        "question": "What is Python?",
        "options": ["Snake", "Programming Language", "Game", "Browser"],
        "answer": "Programming Language"
      }}
    ]

    Content:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    cleaned_response = response.text.strip()

    cleaned_response = cleaned_response.replace("```json", "")
    cleaned_response = cleaned_response.replace("```", "")

    return json.loads(cleaned_response)