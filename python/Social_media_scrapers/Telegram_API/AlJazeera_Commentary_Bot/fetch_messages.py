import logging
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(level=logging.INFO)

# Your API ID, Hash and Bot Token
api_id = '27931942'
api_hash = '2f1d6cfb0a9b788b73491cfa27e489ba'
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# List of channels and their discussion group
source_channels = [
    'https://t.me/aljazeera_world',             # Al Jazeera channel for posts
    'https://t.me/aljazeera_world_discussion',  # Associated discussion group for comments
    'https://t.me/BBCWorldoffl',                # Al Jazeera channel for posts
    'https://t.me/palki_sharma'                 # Palki Sharma's channel for posts
]
target_channel = '@AlJazeera_Commentary_Bot'

# Initialize the client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    logging.info(f"Received message: {event.message.text}")
    # Forward the message to your bot's channel
    await client.send_message(target_channel, event.message)

print("Bot is running...")
client.run_until_disconnected()
