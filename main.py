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
    name = update.message.from_user.first_name
    logger.info(f"El usuario {name} ha iniciado una conversacion")
    update.message.reply_text(f'Hola {name}')


def help_command(update, context):
    update.message.reply_text('necesito ayuda!')

def valid(c):
    return c.isdigit() or c == '+' or c == '-' or c == '*' or c == '/' 

def calcular(update,context):
    name = update.message.from_user.first_name
    try:
        s = ""
        for i in context.args:
            for c in i:
                if(not valid(c)):
                    update.message.reply_text(f"{name} por favor utilice operaciones validas")
                    return
            s = s + i
        update.message.reply_text(f"{name} la respuesta es {calculadora.evaluate(s)}")

    except (ValueError):
        update.message.reply_text(f"{name} por favor utilice operaciones validas")

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