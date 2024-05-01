import os
import jwt
from supabase_py import create_client
from dotenv import load_dotenv

class SupabaseClient:
   
    def __init__(self):
        load_dotenv()

        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')

        self.supabase_client = create_client(supabase_url, supabase_key)

    def get_supabase_client(self):
        return self.supabase_client
        

    def GetuserID(self, jwt_token):
        try:
            #decodificar el token
            payload = jwt.decode(jwt_token,verify=False)

            #obtener el valor del id de usuario
            user_id = payload.get('id')
            return user_id
        
        except jwt.ExpiredSignatureError:
            # Manejar el caso en el que el token JWT haya expirado
            return None
        except jwt.InvalidTokenError:
            # Manejar el caso en el que el token JWT sea inválido
            return None