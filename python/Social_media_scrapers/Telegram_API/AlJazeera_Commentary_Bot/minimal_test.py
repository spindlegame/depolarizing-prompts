from telegram import Bot

# Replace with your bot token
bot_token = 'YOUR_BOT_TOKEN'

# Initialize the bot
bot = Bot(token=bot_token)

# Send a simple message to yourself (replace with your chat ID)
bot.send_message(chat_id='YOUR_CHAT_ID', text="Testing bot response")

print("Message sent")
