import telebot

bot = telebot.TeleBot("7163087906:AAEmvrU6HPIvud-wsWskmpfeYLzSM8bwWTU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)
	
bot.polling( none_stop=True )