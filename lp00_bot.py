from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text = "Hello friend!"
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    lp00_bot = Updater("TOKEN", request_kwargs=PROXY)
    dp = lp00_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    lp00_bot.start_polling()
    lp00_bot.idle()


main()
