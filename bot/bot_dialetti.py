import telegram as tg
from telegram import ext

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Vaffanculo")


start_handler = ext.CommandHandler('start', start)


def debug(update, context):
    keyboard = [[]]
    cols = 2
    n_items = 250

    for label, callback in enumerate(range(n_items)):
        button = tg.InlineKeyboardButton(label, callback_data=callback)
        if len(keyboard[-1])==cols:
            keyboard.append([button])
        else:
            keyboard[-1].append(button)

    keyboard = tg.InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Dio povero', reply_markup=keyboard)


debug_handler = ext.CommandHandler('debug', debug)


def sample(update, context):

    reply_keyboard = [['Bari', 'Lecce']]
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli il comune del tuo dialetto")
    reply_markup=tg.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    update.message.reply_text('Dio cencioso', reply_markup=keyboard)

    return COMUNE


def comune(update, context):
    comune = update.message.text
    print(comune)
    update.message.reply_text('Grande fra, ora manda l\'audio',
                              reply_markup=ReplyKeyboardRemove())
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
    
    return ext.ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Oh no! :(')

    return ext.ConversationHandler.END


VOICE, COMUNE = range(2)

conv_handler = ext.ConversationHandler(
    entry_points=[ext.CommandHandler('sample', sample)],
    
    states = {
        COMUNE: [ext.MessageHandler(ext.Filters.text & ~ext.Filters.command, comune)],
        VOICE: [ext.MessageHandler(ext.Filters.audio | ext.Filters.voice, audio)]
        },
    
    fallbacks = [ext.CommandHandler('cancel', cancel)]
    )

updater = ext.Updater(token='737649334:AAHE_ixL95-wTBFrKvYH4x4ycoj-IwRgYKA', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(debug_handler)
dispatcher.add_handler(conv_handler)

updater.start_polling()

updater.idle()
