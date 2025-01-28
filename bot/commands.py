from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, CallbackContext
import json

from scraping.scraper import imdb_scraper

scraper = imdb_scraper()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Movie & TV Show Tracker Bot! 🎥")

async def search_movie(update: Update, context: CallbackContext):

    movie_name = " ".join(context.args)  # Get user input after the command
    print(movie_name)
    if not movie_name:
        await update.message.reply_text("Please provide a movie name to search.")
        return

    await update.message.reply_text(f"Searching for '{movie_name}'... 🚀")
    
    result = scraper.search_movie(movie_name)
    for movie in result:
        # first send the posture/image
        await update.message.reply_photo(movie['img_url'])
        # then send other movie description

        keyboard = [ [InlineKeyboardButton(f"detail for: {movie['title']}", callback_data=str(movie['detail_url']))] ]
        response = "Title: {title}\nrelease date: {release_date}\nstars: {stars}".format(title=movie['title'],
                                                                                            release_date=movie['release_date'],
                                                                                            stars=movie['stars'])
    

        await update.message.reply_text(response, reply_markup=InlineKeyboardMarkup(keyboard))

async def movie_details(update: Update, context: CallbackContext):
    print("detail command received")
    query = update.callback_query
    movie_detail_url = query.data

    await query.answer()
    await query.edit_message_text(text=f"{movie_detail_url}")

