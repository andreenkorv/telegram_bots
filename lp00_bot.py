from telegram.ext   import Updater

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    LP00_bot = Updater("1008440417:AAFPWHZXGgQ5zeFOkSwdCll0z8LF_xemDcU", use_context=True, request_kwargs=PROXY)
    LP00_bot.start_polling()
    LP00_bot.idle()

main()

