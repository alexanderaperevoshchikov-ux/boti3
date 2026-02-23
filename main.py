import telebot
from pyexpat.errors import messages
import sqlite3

token = "8694316841:AAFag6C4pXcq4A5P7nKeJTzjBcB0dgC3vj8"
bot = telebot.TeleBot(token)
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user_appointment
                (user_id INTEGER, 
                 date TEXT, 
                 client TEXT,
                 PRIMARY KEY (user_id, date))''')

def add_appointment(date,time,client):
    pass
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Дратуте")


if __name__ == '__main__':
    bot.polling(non_stop=True)