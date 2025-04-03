import os
from openai import OpenAI
from config import settings

class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def get_ai_response(self, user_message: str) -> str:

        #Combine eisting converstaion history 
        messages = [
            {"role": "user", "content": user_message}
        ]

        response  = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

        