import config
import telebot

bot = telebot.TeleBot(config.TOKEN)
print(bot.get_me())