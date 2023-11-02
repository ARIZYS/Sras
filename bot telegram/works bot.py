import webbrowser
import telebot
from telebot import types


bot = telebot.TeleBot("6471873793:AAGwJAy5u8Puj8HxIAOyBJegV9P9QaIhrmQ")



@bot.message_handler(commands=["site"])
def site(message):
    webbrowser.open("https://www.youtube.com/@ARIZYS")


@bot.message_handler(commands=["start"])
def get_p(message):
    markup = types.InlineKeyboardMarkup()
    bs = types.InlineKeyboardButton("RKSI", url="https://www.rksi.ru/")

@bot.message_handler(commands=["help"])
def main(message):
        bot.send_message(message.chat.id, "I can help you")

@bot.message_handler(commands=["Happy"])
def site(message):
    webbrowser.open("https://www.youtube.com/watch?v=3EfHQzRKLL0")

@bot.message_handler(commands=["true"])
def main(message):
    bot.send_message(message.chat.id, "Коля пидор")

@bot.message_handler(commands= ["menu"])
def menu(message):
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton("ARIZYS")
    markup.row(b1)
    b2 = types.KeyboardButton("delete photo")
    b3 = types.KeyboardButton("edit")

    markup.row(b3,b2)
    bot.send_message(message.chat.id,"HELLO", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback == "edit":
      bot.edit_message_text("edit text", callback.message.chat.id, callback.message.message_id)



@bot.message_handler(content_types=["message"])
def get_p(message):
    markup = types.InlineKeyboardMarkup()
    buttimes1 = types.InlineKeyboardButton("RKSI", Url= "https://www.rksi.ru/")







bot.polling(none_stop=True)



