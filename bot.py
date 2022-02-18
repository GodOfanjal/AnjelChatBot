import os

API_KEY = os.getenv('API_KEY')

__command_list__ = [
    "start",
]

def start(message):
  bot.reply_text(message, "irukan")
  
  bot.pulling()
