# Coded by @SMDxTG - Modified for Bot Token Deployment

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")

# CHANGE: Replaced USER_SESSION with BOT_TOKEN
# Get your bot token from Telegram's @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "") 

# Web
PORT = int(os.getenv("PORT", "8080")) 
URL = os.getenv("URL", "https://web-production-c02fb5.up.railway.app/") 

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "") # Mongodb Url 
DATABASE_NAME = os.getenv("DATABASE_NAME", "@S95Hub") 

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.cards/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", "-1003919899883"))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", "0"))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", "0"))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://i.ibb.co/7dq7mMLp/photo-2025-10-18-16-42-28-7562603128038621216.jpg") 
BOT_TAG = os.getenv("BOT_TAG", "@S95hub") # File Prefix

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "300"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", 50))  # Default: 50 GB
