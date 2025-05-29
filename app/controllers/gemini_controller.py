from google import genai
import os
from dotenv import load_dotenv

class GeminiController:
    def __init__(self):
        load_dotenv()
        self.genai = genai.Client(api_key = os.getenv('GEMINI_API_KEY'))

    def get_plan_title(self, plan1, plan2, plan3=None):
        prompt = f'''Responde únicamente con un título breve y directo para un plan 
        que incluya {plan1}, {plan2} y {plan3}. El título debe ser único, sin más explicaciones ni opciones.'''
        response = self.genai.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return response.text

    