import telebot
bot = telebot.TeleBot('6629470596:AAGFZlJx2VuPYt8VRST5HSJqAyVKvq1KCsc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!')

@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id, 'Погнали!')

bot.infinity_polling()