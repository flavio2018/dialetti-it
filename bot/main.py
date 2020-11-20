import logging
from telegram import ext
from bot.handlers import *
from bot.config import TOKEN
import os

# Set up the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Set up the port
PORT = int(os.environ.get('PORT', 5000))

# Instance updater and dispatcher
updater = ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the handlers
for handler_name in os.listdir("bot/handlers/"):
    dispatcher.add_handler(eval(handler_name.handler))

# Start the Bot
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN)
updater.bot.setWebhook('https://dialetti-it.herokuapp.com/' + TOKEN)
updater.idle()
