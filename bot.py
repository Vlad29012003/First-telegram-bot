import telebot 
from telebot import types 
import random
from random import randint
# from config import TOKEN
import datetime

bot = telebot.TeleBot('6109603107:AAEK_JeMGxQj44SKsle-5ZOE5rcmLXSrFHY')
@bot.message_handler(commands = ['start'])
def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('рандомное число')
    item2 = types.KeyboardButton('курсы валют')
    item3 = types.KeyboardButton('информация')
    item4 = types.KeyboardButton('другое')
    
    
    
    markup.add (item1,item2,item3,item4)

    
    bot.send_message(message.chat.id,'привет  {0.first_name}!'.format(message.from_user),reply_markup = markup)
    bot.send_photo(message.chat.id,open('static/159768660514539537.jpg',mode='rb'))




@bot.message_handler(content_types=['text'])

# bot.polling(non_stop=True) 

def bot_message (message):
    if message.chat.type == 'private':
        if message.text == 'рандомное число':
            bot.send_message(message.chat.id,'важе число ' + ' ' + str(random.randint(0,10000)))

        elif message.text == 'курсы валют':
            markup = types.ReplyKeyboardMarkup(row_width=3)
            knopka = types.KeyboardButton('доллар-сом 88')
            knopka2 = types.KeyboardButton('евро-сом = 92')
            knopka3 = types.KeyboardButton('<<<<<<')
            markup.add(knopka,knopka2,knopka3,)
            bot.send_message(message.chat.id,'курс валют',reply_markup=markup)

        elif message.text == 'информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            knopka = types.KeyboardButton(f'bot созданн {datetime.datetime.now()},)')
            back = types.KeyboardButton('<<<<<<')
            markup.add(knopka,back)
            bot.send_message(message.chat.id ,'информация о боте', reply_markup=markup)

        elif message.text == 'другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            knopka = types.KeyboardButton('подписи ')
            knopka2= types.KeyboardButton('стикеры')
            back = types.KeyboardButton('<<<<<<')
            markup.add(knopka,knopka2,back)
            bot.send_message(message.chat.id,'другое',reply_markup=markup)

        elif message.text =='<<<<<<':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('рандомное число')
            item2 = types.KeyboardButton('курсы валют')
            item3 = types.KeyboardButton('информация')
            item4 = types.KeyboardButton('другое')

            markup.add(item1,item2,item3,item4)
            bot.send_message(message.chat.id,'<<<<<<',reply_markup=markup)
    
 



bot.polling(non_stop=True)