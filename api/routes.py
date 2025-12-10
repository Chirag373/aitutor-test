from fastapi import APIRouter
from api.models import QuestionRequest, QuestionResponse
from api.search import get_google_search_tool
import google.generativeai as genai
import json

router = APIRouter()

genai.configure(api_key="AIzaSyAF-N7obAkvmchzIdhvxdiCahZJhElHf_w")

@router.post("/generate-question", response_model=QuestionResponse)
async def generate_question(request: QuestionRequest):
    """
    Generate a multiple-choice question from a source text or topic using Gemini 3 and Google Search.
    """
    tool_config = get_google_search_tool()

    model = genai.GenerativeModel('gemini-3-pro-preview', tools=[tool_config])
    
    prompt = f"""
    You are an educational AI. 
    1. Use Google Search to research and verify details about the following source/topic: "{request.source}".
    2. Based on the verified information, create a high-quality multiple-choice question.
    
    Return a valid JSON object (NO markdown, NO code blocks) with the following exact keys:
    - "Question": The question string.
    - "Options": A list of 4 distinct answer choices (strings).
    - "Answer": The correct answer string (must be one of the Options).
    - "Source_URL": Return the title or main URL found during search, or fallback to "{request.source}".
    
    JSON:
    """

    try:
        response = model.generate_content(prompt)
        
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        
        start_idx = cleaned_text.find('{')
        end_idx = cleaned_text.rfind('}') + 1
        if start_idx != -1 and end_idx != -1:
             cleaned_text = cleaned_text[start_idx:end_idx]
             
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
            Question=f"Error generating question for: {request.source}. Details: {str(e)}",
            Options=["Error", "Try", "Again", "Later"],
            Answer="Error",
            Source_URL=request.source
        )
