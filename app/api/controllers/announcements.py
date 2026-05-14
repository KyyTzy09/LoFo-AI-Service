from fastapi import APIRouter, Depends, HTTPException
from app.api.services.announcements_service import AnnouncementsService
from app.models.announcements import createAnnouncementRequest
from app.deps.deps import verify_token
from app.helpers.announcement_converter import CreateAnnouncementConverter


announcements_router = APIRouter()

@announcements_router.post("/create-voice")
def create_announcement(request: createAnnouncementRequest, _: bool = Depends(verify_token), service: AnnouncementsService = Depends()):
    converter = CreateAnnouncementConverter(request)
    try :
        payload = converter.convert()
        response = service.create_announcement_with_voice(payload)
        return {"message": "announcement generated successfully", "success": True, "data" : response } 
    
    except Exception as e:
            raise HTTPException(500, str(e))