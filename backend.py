import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

genai.configure(api_key= KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Tell me about the qualities of a volleyball")
print(response.text)


