from pydantic import BaseModel
from app.models.enums import ItemStatus

class ItemModel(BaseModel):
    itemId: str
    item_name: str
    item_info: str
    image : str
    
    status: str
    user_id: str
    qr_url: str

    created_at: str
    updated_at: str