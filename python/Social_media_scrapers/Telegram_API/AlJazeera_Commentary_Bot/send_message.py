import asyncio
from telegram import Bot

# Use the bot token provided by @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the bot with your token
bot = Bot(token=bot_token)

# Your chat ID
chat_id = '1838982250'

# Define an asynchronous function to send the message
async def send_message():
    await bot.send_message(chat_id=chat_id, text="Hello! This is a test message from your bot.")

# Run the asynchronous function
asyncio.run(send_message())
