import telebot
from pyexpat.errors import messages

token = "8694316841:AAFag6C4pXcq4A5P7nKeJTzjBcB0dgC3vj8"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Дратуте")


if __name__ == '__main__':
    bot.polling(non_stop=True)