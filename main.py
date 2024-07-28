from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def handle_web_app_data(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    web_app_data = message.web_app_data.data
    message.reply_text(f"Datos recibidos desde la Mini App: {web_app_data}")

def main() -> None:
    updater = Updater("7453182687:AAEN1zgb7hdzDCaNjGy4-u-teDAcXVrFUmY")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(filters.web_app_data, handle_web_app_data))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()