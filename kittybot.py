from telegram.ext import Updater, MessageHandler, CommandHandler,  Filters
from telegram import ReplyKeyboardMarkup

updater = Updater(token='7577443930:AAFZ8av_6ztN_8iW4VxTX1CBKkmZO-KUC0s')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    # Вот она, наша кнопка.
    # Обратите внимание: в класс передаётся список, вложенный в список,
    # даже если кнопка всего одна.
    buttons = ReplyKeyboardMarkup([
        ['Который час?', 'Определи мой ip'],
        ['/random_digit']
    ])
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name),
        reply_markup=buttons
    )

# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, say_hi))

updater.start_polling()
updater.idle()