import os
import jwt
from supabase import create_client
from dotenv import load_dotenv
import json
import pandas as pd
from datetime import datetime
import unicodedata

class SupabaseController:

    supabase_token = os.getenv('SUPABASE_JWT')
    
    def __init__(self):
        load_dotenv()

        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY2')
        

        self.supabase_client = create_client(supabase_url, supabase_key)

    def get_supabase_client(self):
        return self.supabase_client
        

    def GetuserID(self, jwt_token):
        try:
            #decodificar el token
            payload = jwt.decode(jwt_token)

            #obtener el valor del id de usuario
            user_id = payload.get('id')
            return user_id
        
        except jwt.ExpiredSignatureError:
            # Manejar el caso en el que el token JWT haya expirado
            return None
        except jwt.InvalidTokenError:
            # Manejar el caso en el que el token JWT sea inválido
            return None
        
    def GetUserIdFromjwt(self,jwt_token):
        try:
            supabase = self.get_supabase_client()
            userjwt = supabase.auth.get_user(jwt_token)
            if userjwt:
                id_usuario = userjwt.user.id
                return id_usuario
            else:
                return None
            
        except Exception as e:
            return None
        
    def GetUserEmailFromjwt(self,jwt_token):
        try:
            supabase = self.get_supabase_client()
            userjwt = supabase.auth.get_user(jwt_token)
            if userjwt:
                user_email = userjwt.user.email
                return user_email
            else:
                return None
            
        except Exception as e:
            return None
        

    def Prueba(self):
        supabase = self.get_supabase_client()
        supabase.auth.sign_in_with_password({"email": "carlos@mail.com", "password": "Rest1234_"})
        session = supabase.auth.get_session().access_token
        return session
    
    def SignOut(self):
        supabase = self.get_supabase_client()
        supabase.auth.sign_out()

    def get_events(self):
        supabase = self.get_supabase_client()
        events = supabase.table('event').select('*').order('id', desc=False).execute()
        return events
    
    def get_events2(self):
        supabase = self.get_supabase_client()
        events = supabase.table('event').select('*').execute()
        return events
    
    def get_today_events(self):
        supabase = self.get_supabase_client()
        today = datetime.today().strftime('%Y-%m-%d')
        events = supabase.table('event').select('*').eq('start_date', today).order('id', desc=False).execute()
        return events

    def get_users(self):
        supabase = self.get_supabase_client()
        profiles = supabase.table('user').select('*').order('id', desc=False).execute()
        users = supabase.auth.admin.list_users()
        ##print(users)
        ids_usuarios = [usuario.id for usuario in users]
        ##print(ids_usuarios)
        users_sorted = sorted(ids_usuarios)
        ##print(users_sorted)
        return users_sorted

    def get_valorations(self):
        supabase = self.get_supabase_client()
        plans = supabase.table('valoration_event').select('*').execute()
        return plans
    
    
    
    def processresponseNoDF(self,response):
        try:
            # Obtener los datos en formato JSON utilizando el método model_dump_json()
            response_json = response.model_dump_json()

            # Convertir los datos en un diccionario
            response_dict = json.loads(response_json)

            # Acceder a los datos de las valoraciones
            valorations_data = response_dict['data']

            return valorations_data

        except Exception as e:
            print("Error:", e)
            return None
        
    def processresponse(self,response):
        try:
            # Obtener los datos en formato JSON utilizando el método model_dump_json()
            response_json = response.model_dump_json()

            # Convertir los datos en un diccionario
            response_dict = json.loads(response_json)

            # Acceder a los datos de las valoraciones
            valorations_data = response_dict['data']

            # Convertir los datos en un DataFrame de Pandas
            df_bien = pd.DataFrame(valorations_data)

            return df_bien

        except Exception as e:
            #print("Error:", e)
            return None
    

    def processresponseusers(self,response):
        try:

            # Convertir los datos en un DataFrame de Pandas
            df_bien = pd.DataFrame(response)

            return df_bien

        except Exception as e:
            #print("Error:", e)
            return None

    def normalizar_texto(self, texto):
        if not texto:
            return ''
        # Eliminar tildes usando unicodedata
        texto_sin_tildes = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        return texto_sin_tildes.lower()