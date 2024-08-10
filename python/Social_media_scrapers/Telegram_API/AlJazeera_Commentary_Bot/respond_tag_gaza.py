from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Replace with your bot token from @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the Application
application = Application.builder().token(bot_token).build()

# Define a function to handle messages containing the keyword "gaza"
async def handle_gaza_keyword(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()
    
    if "gaza" in message_text:
        response_text = "It seems like you're talking about Gaza. Here's some relevant information or updates."
        await update.message.reply_text(response_text)

# Add a message handler to the application
gaza_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_gaza_keyword)
application.add_handler(gaza_handler)

# Start the bot
application.run_polling()
