from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/ping")
def Pong():
    return {"message": "Pong", "success": True}
@api_router.get("/test")
def test():
    return {"message": "Siam mokel", "success": True}