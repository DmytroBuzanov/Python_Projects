from telethon import TelegramClient, sync
from .config import *

client = TelegramClient(phototime, api_id, api_hash)
client.start()
