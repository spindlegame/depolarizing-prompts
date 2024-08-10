import logging
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot token from @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Initialize the Application
application = Application.builder().token(bot_token).build()

# Define a function to fetch and save messages
async def fetch_messages(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_count = 10  # Adjust this value as needed
    messages = []

    # Manually fetch updates (assuming these are the latest available)
    updates = await context.bot.get_updates(limit=message_count)
    
    # Filter messages from the specific chat
    for update in updates:
        if update.message and update.message.chat.id == chat_id:
            messages.append(update.message.to_dict())  # Convert message to a dictionary and append to the list

    # Save the messages to a file
    with open('D:/SCRIPTS/python/Social_media_scrapers/Telegram_API/AlJazeera_Commentary_Bot/messages.json', 'w') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)

    await update.message.reply_text(f"{len(messages)} messages have been saved to 'messages.json'.")

# Add a command handler to trigger fetching messages
fetch_handler = CommandHandler('fetch', fetch_messages)
application.add_handler(fetch_handler)

# Start the bot
application.run_polling()
