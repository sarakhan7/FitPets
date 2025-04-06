import google.generativeai as genai

# Configure Gemini AI with your API key (good job already doing this!)
genai.configure(api_key="AIzaSyAwy-NqGiS5HsG1IQ0Y418VOTL86PTTCY8")

def get_tips_from_gemini_ai(tasks):
    """
    Generate tips using Gemini AI based on the user's to-do list.
    """
    task_titles = [task.title for task in tasks]

    if not task_titles:
        return ["You have no tasks right now. Try adding some!"]

    prompt = (
        "Based on this user's to-do list:\n"
        + "\n".join(f"- {title}" for title in task_titles)
        + "\n\nGive helpful productivity or organization tips."
    )

    try:
        model = genai.GenerativeModel("gemini-2.0-flash-001")
        response = model.generate_content(prompt)
        # Split and clean lines from response
        tips = [line.strip("-• ") for line in response.text.strip().splitlines() if line.strip()]
        return tips
    except Exception as e:
        print(f"Error calling Gemini AI: {e}")
        return ["Could not fetch tips at this time."]