from fastapi import APIRouter, Depends, HTTPException
from app.ai.llm.client import aiClient as model
from app.ai.llm.loader import load_prompt
import json
from pydantic import BaseModel
from app.api.services.announcements_service import AnnouncementsService
from app.models.announcements import createAnnouncementRequest
from app.deps.deps import verify_token


announcements_router = APIRouter()

@announcements_router.post("/create-voice")
def create_announcement(request: createAnnouncementRequest, _: bool = Depends(verify_token), service: AnnouncementsService = Depends()):
    try :
        response = service.create_announcement_with_voice(request)
        return {"message": "announcement generated successfully", "success": True, "data" : response } 
    
    except Exception as e:
            raise HTTPException(500, str(e))