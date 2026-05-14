from pydantic import BaseModel
from typing import List, Optional
from app.models.item_model import ItemModel

class Announcement(BaseModel):
    announcementId: str
    
    title: str
    description: str
    location: str
    lost_at: str
    
    user_id: str
    item_id: Optional[str] 
    
    created_at: str
    updated_at: str

class createAnnouncementRequest(BaseModel):
    text: str
    connect_item: bool
    items: Optional[List[ItemModel]]