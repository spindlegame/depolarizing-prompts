# It looks like the Updater class in the python-telegram-bot library has undergone changes,
# and the way you initialize it has been updated in the newer versions.
# The error you are seeing indicates that the 'token' argument is no longer valid in the
# Updater initialization. The correct approach now is to use the Application class with
# a builder pattern and to handle async functions properly.


from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot token from @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the Application (replaces Updater in version 20+)
application = Application.builder().token(bot_token).build()

# Define a start command handler function
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! The bot is working!')

# Add the start command handler to the application
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Start the bot
application.run_polling()
