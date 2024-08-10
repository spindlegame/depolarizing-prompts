from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot token from @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the Application (replaces Updater in version 20+)
print("Initializing bot...")
application = Application.builder().token(bot_token).build()

# Define a start command handler function
async def start(update: Update, context: CallbackContext) -> None:
    print("Start command received.")
    chat_id = update.message.chat_id
    print(f"Chat ID is: {chat_id}")
    await update.message.reply_text(f"Your chat ID is: {chat_id}")

# Add the start command handler to the application
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Start the bot
print("Starting the bot...")
application.run_polling()
print("Bot is running. Please interact with it in Telegram.")
