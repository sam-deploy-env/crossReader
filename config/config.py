from dotenv import load_dotenv
import os

# Charge les variables d'environnement depuis le fichier .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

DISCORD_GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
PC_NAME = os.getenv("PC_NAME")
