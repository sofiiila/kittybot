import os
from dotenv import load_dotenv
from telegram.ext import Updater

load_dotenv()

secret_token = os.getenv('TOKEN')
# Взяли переменную TOKEN из пространства переменных окружения
...

# Шпионы печальны, шпионы ушли с пустыми руками
updater = Updater(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'
