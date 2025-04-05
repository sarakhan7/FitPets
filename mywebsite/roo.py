import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env!")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Use Gemini Pro model
model = genai.GenerativeModel(model_name="gemini")

print("Roo (Gemini) is ready! Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = model.generate_content(prompt)
    print("Roo:", response.text)
