import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

print("WiFiSentinel Telegram license bot")
print("Developer:", os.getenv("DEVELOPER", "Arman YB"))

if not BOT_TOKEN:
    print("BOT_TOKEN is not configured.")
    print("Create .env from .env.example before starting the bot.")
