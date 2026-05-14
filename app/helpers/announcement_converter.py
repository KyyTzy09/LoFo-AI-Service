from app.models.announcements import createAnnouncementRequest
from pydantic import BaseModel

class AIItem(BaseModel):
    itemId: str
    item_name: str
    item_info: str

class CreateAnnouncementConverter:
    def __init__(self, request: createAnnouncementRequest):
        self.request = request

    def map_items(self):
        items = self.request.items or []
        return [
            AIItem(
                itemId=item.itemId,
                item_name=item.item_name,
                item_info=item.item_info
            ).model_dump()
            for item in items
            ]

    def convert(self):
        request = self.request
        items = self.map_items() if request.connect_item else []

        return {
            "text": self.request.text,
            "items": items,
            "connect_item": self.request.connect_item,
        }
