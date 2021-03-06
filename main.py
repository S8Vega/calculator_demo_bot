import logging
import calculadora
import os
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN_TELEGRAM_CALCULATOR")
mode = os.getenv("MODE")

if mode == "dev":
    def run(updater):
        updater.start_polling()
        print("bot cargado")
        updater.idle()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
else:
    logger.info("No se especifico el MODE")
    sys.exit()

def start(update, context):
    name = update.message.from_user.first_name
    logger.info(f"El usuario {name} ha iniciado una conversacion")
    mensaje = f"Hola {name}, soy una calculadora en Telegram, puedo resolver operaciones matematicas basicas, para mayor informacion utiliza /help"
    update.message.reply_text(mensaje)


def help_command(update, context):
    name = update.message.from_user.first_name
    mensaje = f"""
    Hola {name}, veo que necesitas ayuda, el comando para resolver las operaciones es /calcular seguido de la operacion que se desee realizar
    por ejemplo:
    /calcular 2+1
    /calcular 2*(9-5)
    /calcular 9*(999999999*18)-98
    """
    update.message.reply_text(mensaje)

def valid(c):
    return c.isdigit() or c == '+' or c == '-' or c == '*' or c == '/' or c == '(' or c == ')'

def calcular(update,context):
    name = update.message.from_user.first_name
    try:
        s = ""
        for i in context.args:
            for c in i:
                if(not valid(c)):
                    print(c)
                    update.message.reply_text(f"{name} por favor utilice operaciones validas")
                    return
            s = s + i
        print(s)
        if len(s) == 0:
            update.message.reply_text(f"{name} por favor digite una operacion valida")
        else:
            update.message.reply_text(f"{name} la respuesta es {calculadora.evaluate(s)}")

    except (ValueError):
        update.message.reply_text(f"{name} por favor utilice operaciones validas")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("calcular", calcular))

    run(updater)

if __name__ == '__main__':
    main()