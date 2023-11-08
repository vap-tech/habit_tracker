import requests

from config.settings import TELEGRAM_BOT_TOKEN as TOKEN, TELEGRAM_MY_CHAT_ID as CHAT_ID


def send_telegram_message(chat_id=CHAT_ID, text='example text'):
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
