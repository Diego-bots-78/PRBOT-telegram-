from telegram.ext import Updater, CommandHandler
import os TOKEN = os.getenv('TOKEN')
def start(update, context):
    update.message.reply_text("¡Bot activo desde la nube! ⚡")
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
print("Bot en línea...")
