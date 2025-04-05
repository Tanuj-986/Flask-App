from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

api_key = os.getenv("API_KEY")

client = Groq(api_key=api_key)