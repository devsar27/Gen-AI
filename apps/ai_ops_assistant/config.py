from dotenv import load_dotenv
import os

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Add more settings here as the project grows
# e.g. MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-4")
