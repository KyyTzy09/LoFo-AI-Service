from fastapi import APIRouter, Depends, HTTPException
from app.ai.llm.client import aiClient as model
from app.ai.llm.loader import load_prompt
from pydantic import BaseModel


announcements_router = APIRouter()

class AnnouncementRequest(BaseModel):
    prompt: str

@announcements_router.post("/create-voice")
def create_announcement(request: AnnouncementRequest ):
    try :
        prompt = request.prompt
        response = model.generate(prompt)
        return {"message": response, "success": True} 

    except Exception as e:
            raise HTTPException(500, str(e))