from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Replace with your bot token from @BotFather
bot_token = '7334856578:AAHMIeACt6gd1i7rDUQEN-NgKzKYqFBRMEs'

# Initialize the Application
application = Application.builder().token(bot_token).build()

# Define a function to handle messages containing specific keywords
async def handle_keywords(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()
    response_text = ""

    # Check for each keyword and append the corresponding response
    if "gaza" in message_text:
        response_text += "It seems like you're talking about Gaza. Here's some relevant information or updates.\n"
    if "ukraine" in message_text:
        response_text += "You mentioned Ukraine. Here's the latest on that situation.\n"
    if "covid" in message_text:
        response_text += "You mentioned COVID-19. Here's some information about the pandemic.\n"

    # If no keywords were found, provide a default response
    if response_text == "":
        response_text = "I'm here to help with information on various topics. What would you like to know?"

    await update.message.reply_text(response_text)

# Add a message handler to the application
keywords_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keywords)
application.add_handler(keywords_handler)

# Start the bot
application.run_polling()

with open('D:/SCRIPTS/python/Social_media_scrapers/Telegram_API/AlJazeera_Commentary_Bot/messages.json', 'w') as file:
    json.dump(messages, file, ensure_ascii=False, indent=4)

