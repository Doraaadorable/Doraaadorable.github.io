import os
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print("API key loaded:", api_key)
print("Database URL loaded:", db_url)
