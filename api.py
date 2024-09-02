import telebot
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)
	
bot.polling( none_stop=True )