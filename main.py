from telegram.ext import Application, CommandHandler
from config import TELEGRAM_API_TOKEN

from bot.commands import start, search_movie

# Create Application and pass the Telegram API token
application = Application.builder().token(TELEGRAM_API_TOKEN).build()

# Bot Command Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("movie", search_movie))
# Start the bot
application.run_polling()