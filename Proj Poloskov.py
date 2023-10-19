import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot("6471873793:AAGwJAy5u8Puj8HxIAOyBJegV9P9QaIhrmQ")

@bot.message_handler(commands= ["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton("ARIZYS")
    markup.row(b1)
    b2 = types.KeyboardButton("delete photo")
    markup.row(b2)
    b3 = types.KeyboardButton("edit")
    markup.row(b3)
    bot.send_message(message.chat.id,"HELLO", reply_markup=markup)

    bot.polling(none_stop=True)