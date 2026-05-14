
import json
from datetime import datetime
from app.ai.llm.client import aiClient as model
from typing import List
from app.ai.llm.loader import load_prompt
from app.models.announcements import createAnnouncementRequest
import pytz
from app.helpers.date_helper import GetDay


class AnnouncementsService:
    def __init__(self):
        # Initialize any necessary resources, such as database connections
        pass


    def create_announcement_with_voice(self, payload: dict):
        try:
            wib = pytz.timezone("Asia/Jakarta")
            now = datetime.now(wib).isoformat()
            today = GetDay(datetime.now(wib))
            
            prompt_tmplt = load_prompt("create_announcement.prompt")
            prompt = prompt_tmplt.replace(
                "{{payload_json}}",
                json.dumps(payload, ensure_ascii=False, indent=2)
            ).replace(
                "{{current_time}}",
                now
            ).replace(
                "{{today}}",
                today
            )
        
            response = model.generate(prompt)
            clean = response.replace("```json", "").replace("```", "").strip()
            
            result = json.loads(clean)
            return result
        except Exception as e:
            raise Exception(f"Failed to create announcement: {str(e)}")