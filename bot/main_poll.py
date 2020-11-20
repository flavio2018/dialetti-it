import logging
from telegram import ext
from bot.handlers import *
from bot.token import TOKEN
import os

# Set up the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Instance updater and dispatcher
updater = ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


for handler_name in os.listdir("bot/handlers/"):
    dispatcher.add_handler(exec(handler_name.handler))

# Start the Bot
updater.start_polling()
updater.idle()
