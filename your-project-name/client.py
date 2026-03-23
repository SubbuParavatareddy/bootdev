from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
# Only run this block for Gemini Developer API
client = genai.Client(api_key=api_key)
#print(client)
