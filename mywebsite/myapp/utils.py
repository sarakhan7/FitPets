import google.generativeai as genai
from django.core.cache import cache

# Configure Gemini AI with your API key (good job already doing this!)
genai.configure(api_key="AIzaSyAwy-NqGiS5HsG1IQ0Y418VOTL86PTTCY8")

from django.core.cache import cache
import google.generativeai as genai

# Configure Gemini AI with your API key
genai.configure(api_key="AIzaSyAwy-NqGiS5HsG1IQ0Y418VOTL86PTTCY8")

def get_tips_from_gemini_ai(tasks):
    """
    Generate tips using Gemini AI based on the user's to-do list, with caching to improve performance.
    """
    # Create a cache key based on the task titles to uniquely identify the cache for these tasks
    task_titles = [task.title for task in tasks]
    
    if not task_titles:
        return ["You have no tasks right now. Try adding some!"]

    # Cache key is a combination of task titles to uniquely identify the tips for this set of tasks
    cache_key = "gemini_tips_" + "_".join(task_titles)

    # Try to get the cached tips
    cached_tips = cache.get(cache_key)
    if cached_tips:
        return cached_tips

    # If no cached tips, proceed to generate new tips from Gemini AI
    prompt = (
        "Based on this user's to-do list:\n"
        + "\n".join(f"- {title}" for title in task_titles)
        + "\n\nGive tips on how to achieve these tasks in the to do list. Make it very concise, with each tip only being 1-2 lines."
        + "\n\nAlso, do not include anything similar to 'Okay, here are some concise tips to achieve each goal:', only include the tips themselves."
    )

    try:
        model = genai.GenerativeModel("gemini-2.0-flash-001")
        response = model.generate_content(prompt)
        
        # Split and clean lines from the response
        tips = [line.strip("-• ") for line in response.text.strip().splitlines() if line.strip()]
        
        # Cache the new tips for future use (cache for 5 minutes)
        cache.set(cache_key, tips, timeout=300)  # Cache for 5 minutes

        return tips
    except Exception as e:
        print(f"Error calling Gemini AI: {e}")
        return ["Could not fetch tips at this time."]