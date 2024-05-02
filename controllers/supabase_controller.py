import os
from supabase import create_client
from dotenv import load_dotenv

class SupabaseController:
   
    def __init__(self):
        load_dotenv()

        supabase_url = os.getenv('EXPO_PUBLIC_SB_API_REST_URL')
        supabase_key = os.getenv('EXPO_PUBLIC_SB_API_KEY')

        self.supabase_client = create_client(supabase_url, supabase_key)

    def get_supabase_client(self):
        return self.supabase_client
        
    def GetUserIdFromjwt(self,jwt_token):
        supabase = self.get_supabase_client()
        userjwt = supabase.auth.get_user(jwt_token)
        #print(userjwt)
        if userjwt:
            id_usuario = userjwt.user.id
            return id_usuario
        else:
            return None