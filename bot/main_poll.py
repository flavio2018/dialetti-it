import os
import sys
sys.path.insert(1, "bot/")
import logging
from telegram import ext
import handlers
from config import TOKEN

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
    if ".py" in handler_name:
        dispatcher.add_handler(eval("handlers." + handler_name[:-3]).handler)

# Start the Bot
updater.start_polling()
updater.idle()
