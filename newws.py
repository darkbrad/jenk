import telebot
import json
import requests
bot = telebot.TeleBot('1463531223:AAG1No806z_cKlEl-guhmLHjm_mKSfVDy9A');
#res = requests.get('')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите номер телефона ')
@bot.message_handler(content_types=['text'])
def a(message):
    if '+' in message.text:
       bot.send_contact(message.from_user.id,message.text,'contact')
    else:bot.send_message(message.from_user.id,'Что-то пошло не так:(Попробуйте снова')
bot.polling()