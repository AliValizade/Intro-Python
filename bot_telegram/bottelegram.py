import telebot
import random
from telebot import types



bot = telebot.TeleBot("5310910885:AAEz17DqK4hc2m40h456ga0fLtxWWNaaJqw")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi dear, welcome to Guess_Number Game.")

@bot.message_handler(commands=['New_Game'])
def send_welcome(message):
    bot.reply_to(message, "Please enter a number between 1 & 100 :")
    r = random.randint(0, 100)

    @bot.message_handler(func= lambda m: True)
    def echo(message):
        #myname = message.from_user.first_name
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('x')
        x = int(message.text)
        if x==r:
            bot.reply_to(message,"Congrajulation, You Win✅❤")
        elif x<r:
            bot.reply_to(message,"Go up⏫")
        elif x>r: 
            bot.reply_to(message,"Go down⏬")

    
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Send this keys to play with me: /start  ,  /help , /New_Game  ,  /bye  .  ")

@bot.message_handler(commands=['bye'])
def send_welcome(message):
    bot.reply_to(message, "Say hello to your aunt💘✅ ")

@bot.message_handler(commands=['fal'])
def send_message(message):
    fal_list = ['به فنا خواهی رفت', 'به دیدار معشوق خواهی رفت', 'به سفر خواهی رفت']
    fal = random.choice(fal_list)
    bot.reply_to(message, fal)


bot.infinity_polling()



