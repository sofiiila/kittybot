import requests
from telegram import Bot

bot = Bot(token='7577443930:AAFZ8av_6ztN_8iW4VxTX1CBKkmZO-KUC0s')

URL = 'https://api.thecatapi.com/v1/images/search'

chat_id = 443566057

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)
