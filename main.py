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
    update.message.reply_text('Hola amigos!!')


def help_command(update, context):
    update.message.reply_text('necesito ayuda!')



def calcular(update,context):
    try:
        s = ""
        for i in context.args:
            s = s + i
        update.message.reply_text(f"La respuesta es {calculadora.evaluate(s)}")

    except (ValueError):
        update.message.reply_text("por favor utilice operaciones validas")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("calcular", calcular))
    
    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()