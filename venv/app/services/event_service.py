import os
from app.models import Event
from supabase_py import create_client
from dotenv import load_dotenv

class EventService:
        def __init__(self):
            load_dotenv()

            supabase_url = os.getenv('SUPABASE_URL')
            supabase_key = os.getenv('SUPABASE_KEY')

            self.supabase = create_client(supabase_url,supabase_key)
        
        #obtener los eventos si no me equivoco directamente de la respuesta
        #del algoritmo
        def get_events(self, user_location, date, category):
            eventos = [
                Event(
                    id=1,
                    price=100,
                    status=None,
                    latitude=39.471373,
                    longitude=-0.386638,
                    name="Evento de ejemplo",
                    description="Una descripción de ejemplo",
                    start_at="2024-04-22T21:46:38.536882+00:00",
                    end_at="2024-04-22T21:46:38.536882+00:00",
                    created_by=5,
                    created_at="2024-04-22T21:46:38.536882+00:00",
                    updated_at="2024-04-22T21:46:38.536882+00:00",
                    score=4.2,
                    categories=["ejemplo", "categoria"],
                    gallery=["https://img.image.com/1", "https://img.image.com/2"]
               ),
            # Más eventos...
            ]
        
            return eventos