from telegram import ext

def debug(update, context):
    update.message.reply_text("Vaffanculo", quote=False)

handler = ext.CommandHandler("debug", debug)
