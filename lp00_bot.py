from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import datetime
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text = "Hello friend!"
    update.message.reply_text(text)


def planet_in_stellaris(bot, update):
    user_text = (update.message.text).split()
    user_planet = user_text[1].title()
    cur_date = '{:%Y/%m/%d}'.format(datetime.now())
    print(user_planet)
    if user_planet.lower() == 'mars':
        update.message.reply_text(ephem.constellation(ephem.Mars(cur_date)))
    elif user_planet.lower() == 'venus':
        update.message.reply_text(ephem.constellation(ephem.Venus(cur_date)))
    elif user_planet.lower() == 'saturn':
        update.message.reply_text(ephem.constellation(ephem.Saturn(cur_date)))
    elif user_planet.lower() == 'mercury':
        update.message.reply_text(ephem.constellation(ephem.Mercury(cur_date)))
    elif user_planet.lower() == 'uranus':
        update.message.reply_text(ephem.constellation(ephem.Uranus(cur_date)))
    elif user_planet.lower() == 'jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter(cur_date)))
    elif user_planet.lower() == 'neptune':
        update.message.reply_text(ephem.constellation(ephem.Nupiter(cur_date)))
    else:
        update.message.reply_text(f'Планеты: {user_planet} нету')


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def get_token(file_path):
    file_token = open(file_path)
    TOKEN = file_token.readline()
    file_token.close()
    return TOKEN


def main():
    TOKEN = get_token('lp00_bot.txt')

    lp00_bot = Updater(
                    token=TOKEN[:-1],
                    request_kwargs=PROXY
                    )
    dp = lp00_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_in_stellaris))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    lp00_bot.start_polling()
    lp00_bot.idle()


main()
