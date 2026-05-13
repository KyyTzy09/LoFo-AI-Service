from google import genai
from google.genai import types

from app.ai.llm.loader import load_prompt
from app.configs.config import settings


class GeminiClient:
    def __init__(
        self,
        gemini_model_name: str = "gemini-2.5-flash",
        gemini_fallback_name: str = "gemini-3-flash",
        temperature: float = 0.6,
        max_output_tokens: int = 2021,
        root_prompt: str = load_prompt("root_prompt.prompt"),
    ):
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self.root_prompt = root_prompt
        self.gemini_model_name = gemini_model_name
        self.gemini_fallback_name = gemini_fallback_name

        self.client = genai.Client(api_key=settings.gemini_api_key)

    def generate(self, prompt: str):

        try:
            res = self.client.models.generate_content(
                model=self.gemini_model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=self.temperature,
                    max_output_tokens=self.max_output_tokens,
                    system_instruction=self.root_prompt,
                ),
            )

            if res and res.text:
                return res.text.strip()

            raise RuntimeError("Empty response from Gemini")

        except Exception as e:
            print("Primary Gemini failed:", e)

        # fallback model
        res = self.client.models.generate_content(
            model=self.gemini_fallback_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=self.temperature,
                max_output_tokens=self.max_output_tokens,
                system_instruction=self.root_prompt,
            ),
        )

        if not res or not res.text:
            raise RuntimeError("Gemini fallback also failed")

        return res.text.strip()


aiClient = GeminiClient()