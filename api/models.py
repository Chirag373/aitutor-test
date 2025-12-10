from pydantic import BaseModel, Field
from typing import List

class QuestionRequest(BaseModel):
    source: str

class QuestionResponse(BaseModel):
    Question: str
    Options: List[str]
    Answer: str
    Source_URL: str
