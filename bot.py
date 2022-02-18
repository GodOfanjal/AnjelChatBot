import os

API_KEY = os.getenv('API_KEY')
bot = telebot.telebot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_text(message, "irukan")
  
  bot.pulling()
