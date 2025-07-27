import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

def get_groq_api_key():
    return os.getenv("GROQ_API_KEY")
