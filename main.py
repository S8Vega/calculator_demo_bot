import logging
import calculadora
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN_TELEGRAM_CALCULATOR")

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola amigos!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('necesito ayuda!')



def calcular(update,context):
    try:
        c = calculadora.Calculadora()
        s = ""
        for i in context.args:
            s = s + i
        update.message.reply_text(f"La respuesta es {c.evaluate(s)}")

    except (ValueError):
        update.message.reply_text("por favor utilice operaciones validas")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler("calcular", calcular))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()