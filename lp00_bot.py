from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import datetime
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

city_list = [
    "Москва", "Архангельск", "Норильск", "Канск", "Кисловодск", "Арзамас"
            ]

def cities_game(bot, update):
    city = city_list
    user_city = update.message.text.split()[1]
    try:
        city.remove(user_city)
    except ValueError:
        

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text = "Hello friend!"
    update.message.reply_text(text)


def planet(bot, update):
    planet_name = update.message.text.split()[1]
    cur_date = '{:%Y/%m/%d}'.format(datetime.now())
    print(planet_name)

    planet_name_for_ephem = getattr(ephem, planet_name)(cur_date)
    planet_name_for_ephem.compute()
    constellation_of_the_planet = ephem.constellation(planet_name_for_ephem)

    reply = f'Планета {planet_name} находится в созвездии {constellation_of_the_planet[1]}'
    return update.message.reply_text(reply)


def talk_to_me(bot, update):
    user_text = update.message.text.split()
    print(user_text)
    update.message.reply_text(user_text[:])


def wordcount(bot, update):  # Считает количество слов
    user_text = update.message.text.split()[1:]
    print(user_text)
    if user_text:
        answer = len(user_text)
    else:
        answer = "Введите текст"
    update.message.reply_text(answer)


def next_full_moon(bot, update):  # Когда следующее полнолуние
    user_text = update.message.text.split()[1:]
    print(user_text)
    # if user_text:
    try:
        answer = ephem.next_full_moon(user_text[0])
    except ValueError:
        answer = "введите дату в формате: year/month/day; year-month-day"
    # else:
        # answer = "Введите дату"
    update.message.reply_text(answer)


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
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    lp00_bot.start_polling()
    lp00_bot.idle()


main()
