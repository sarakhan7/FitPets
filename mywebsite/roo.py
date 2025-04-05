import os
import google.generativeai as genai
from dotenv import load_dotenv
import subprocess

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env!")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Use Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-2.0-pro-exp")

# Define your project directory path
project_directory = os.getcwd()

# Function to save generated code to a specific file
def save_code_to_file(file_path, code):
    with open(file_path, 'w') as file:
        file.write(code)
    print(f"Code saved to {file_path}")

# Example: Generate Django model
def generate_django_model():
    prompt = """
    Generate a Django model for a simple blog application. The model should include:
    - title (CharField)
    - content (TextField)
    - created_at (DateTimeField)
    """
    response = model.generate_content(prompt)
    code = response.text

    # Save the generated model to models.py in myapp directory
    model_file_path = os.path.join(project_directory, 'myapp', 'models.py')
    save_code_to_file(model_file_path, code)

# Function to run Django commands
def run_django_command(command):
    subprocess.run(command, shell=True, check=True)
    print(f"Executed: {command}")

# Command loop
print("Roo (Gemini) is ready! Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # If user asks to generate Django model
    if "generate model" in prompt.lower():
        generate_django_model()
        run_django_command("python manage.py makemigrations")
        run_django_command("python manage.py migrate")
    
    # Ask Roo for other types of code generation or tasks
    else:
        response = model.generate_content(prompt)
        print("Roo:", response.text)
