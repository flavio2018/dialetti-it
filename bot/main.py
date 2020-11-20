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

# Set up the port
PORT = int(os.environ.get('PORT', 5000))

# Instance updater and dispatcher
updater = ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the handlers
for handler_name in os.listdir("bot/handlers/"):
    if ".py" in handler_name:
        dispatcher.add_handler(eval("handlers." + handler_name[:-3]).handler)

# Start the Bot
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN)
updater.bot.setWebhook('https://dialetti-it.herokuapp.com/' + TOKEN)
updater.idle()
