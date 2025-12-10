from fastapi import APIRouter
from api.models import QuestionRequest, QuestionResponse
import google.generativeai as genai
import json

router = APIRouter()

genai.configure(api_key="AIzaSyAF-N7obAkvmchzIdhvxdiCahZJhElHf_w")

@router.post("/generate-question", response_model=QuestionResponse)
async def generate_question(request: QuestionRequest):
    """
    Generate a multiple-choice question from a source text or topic using Gemini.
    """
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    prompt = f"""
    You are an educational AI. Create a multiple-choice question based on the following source:
    
    SOURCE: "{request.source}"
    
    Return a valid JSON object (NO markdown, NO code blocks) with the following exact keys:
    - "Question": The question string.
    - "Options": A list of 4 distinct answer choices (strings).
    - "Answer": The correct answer string (must be one of the Options).
    - "Source_URL": Simply return the string "{request.source}".
    
    JSON:
    """

    try:
        response = model.generate_content(prompt)
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(cleaned_text)
        
        return QuestionResponse(
            Question=data["Question"],
            Options=data["Options"],
            Answer=data["Answer"],
            Source_URL=data["Source_URL"]
        )
    except Exception as e:
        print(f"Error generating question: {e}")
        return QuestionResponse(
            Question="Error generating question related to: " + request.source,
            Options=["Error", "Try", "Again", "Later"],
            Answer="Error",
            Source_URL=request.source
        )
