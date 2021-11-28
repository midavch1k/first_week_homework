import logging
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from collections import Counter

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь!')

"""
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
"""
    
def planet_const(update, context):
    
    planets = {
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus, 
        'Mars': ephem.Mars,
        'Jupiter': ephem.Jupiter, 
        'Saturn': ephem.Saturn,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
        'Pluto': ephem.Pluto
    }
    
    user_text = update.message.text.split(' ')[1]
    print (user_text)
    if user_text in planets:
        
        c = ephem.constellation(planets[user_text](2021/11/27))
        update.message.reply_text(', '.join(c))
    

def main():
    my_bot = Updater(settings.API_KEY, use_context = True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_const))
    dp.add_handler(MessageHandler(Filters.text, planet_const))
    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()

if __name__ == '__main__':
    main()