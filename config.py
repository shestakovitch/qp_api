import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.quizplease.ru/api"

TITLE = os.getenv("TITLE")
CAPTAIN = os.getenv("CAPTAIN")
EMAIL = os.getenv("EMAIL")
PHONE = os.getenv("PHONE")
PEOPLE_COUNT = os.getenv("PEOPLE_COUNT")
TELEGRAM_NAME = os.getenv("TELEGRAM_NAME")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
