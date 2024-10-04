from telegram import Bot

bot = Bot(token='7577443930:AAFZ8av_6ztN_8iW4VxTX1CBKkmZO-KUC0s')

URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

chat_id = 443566057
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, URL)
