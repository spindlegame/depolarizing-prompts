from telethon import TelegramClient, events

# Your API ID, Hash and Bot Token
api_id = '27931942'
api_hash = '2f1d6cfb0a9b788b73491cfa27e489ba'
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Source channel and target bot channel
source_channel = 'https://t.me/aljazeera_world'
target_channel = '@AlJazeera_Commentary_Bot'

# Initialize the client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    # Forward the message to your bot's channel
    await client.send_message(target_channel, event.message)

print("Bot is running...")
client.run_until_disconnected()
