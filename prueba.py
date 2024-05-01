import asyncio
from supabase import create_client
import os
from dotenv import load_dotenv


load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

supabase.auth.sign_in_with_password({"email": "carlos@mail.com", "password": "Rest1234_"})

data = supabase.auth.get_user()
print(data)
res2 = supabase.auth.sign_out()
