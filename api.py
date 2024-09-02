import telebot
import environ

bot = telebot.TeleBot(env('TG_TOKEN'))

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)
	
bot.polling( none_stop=True )