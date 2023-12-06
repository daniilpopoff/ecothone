import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOCKEN = os.getenv("BOT_TOCKEN")

bot = telebot.TeleBot(BOT_TOCKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "SHut up i m working")

@bot.message_handler(func= lambda  msg : True )
def echo(message):
    bot.reply_to(message, message.text)




bot.infinity_polling()