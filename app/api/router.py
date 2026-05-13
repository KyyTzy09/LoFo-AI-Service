from fastapi import APIRouter
from app.api.announcements.announcements import announcements_router

api_router = APIRouter()

api_router.include_router(announcements_router, prefix="/announcements", tags=["announcements"])

@api_router.get("/ping")
def Pong():
    return {"message": "Pong", "success": True}
@api_router.get("/test")
def test():
    return {"message": "Siam mokel", "success": True}
