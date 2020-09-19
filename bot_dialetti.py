from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# define callback functions to be nested

def sample(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Manda l'audio fra")
    print('qui ok')
    
    return VOICE
    
def audio(update, context):
    print('audio ok')
    user = update.message.from_user
    print(type(update.message.voice))
    print(f"durata: {update.message.voice.duration}")
    audio_file = update.message.voice.get_file()
    audio_file.download('audio_file.mp3')
    logger.info("User %s sent an audio file", user.first_name)
    update.message.reply_text('Grazie bomber')
    
    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

VOICE = 0

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('sample', sample)],
    
    states = {
        0: [MessageHandler(Filters.audio | Filters.voice, audio)]
        },
    
    fallbacks = [CommandHandler('cancel', cancel)]
    )

updater = Updater(token='737649334:AAHE_ixL95-wTBFrKvYH4x4ycoj-IwRgYKA', use_context=True)
dispatcher = updater.dispatcher

#start_handler = CommandHandler('start', start)
#dispatcher.add_handler(start_handler)

#echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#dispatcher.add_handler(echo_handler)

dispatcher.add_handler(conv_handler)

updater.start_polling()

updater.idle()
