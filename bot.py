from telebot import TeleBot
from structure import register_handlers
#from admin_structure import admin

API_TOKEN = '7058125954:AAEsyLqQbDnf0dFaiwaXmzo424WSx1RcmIg'

bot = TeleBot(API_TOKEN)

# Регистрируем все хендлеры
register_handlers(bot)
#admin(bot)

# Запуск бота
bot.polling()