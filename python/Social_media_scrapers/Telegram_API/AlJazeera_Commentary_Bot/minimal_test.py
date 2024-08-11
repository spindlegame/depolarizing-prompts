from telegram import Bot

# Replace with your bot token
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the bot
bot = Bot(token=bot_token)

# Send a simple message to yourself (replace with your chat ID)
bot.send_message(chat_id='1838982250', text="Testing bot response")

print("Message sent")
