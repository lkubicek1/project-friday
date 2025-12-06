import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Available Models:")
for m in client.models.list():
    if m.supported_actions and 'generateContent' in m.supported_actions:
        print(m.name)
