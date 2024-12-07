from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция, которая будет отправлять сообщение "Привет мир"
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет мир')

def main():
    # Вставь сюда свой токен
    token = '"7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8"
    
    # Создаем объект Updater и передаем токен
    updater = Updater(token)

    # Получаем диспетчер для обработки команд
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать до принудительной остановки
    updater.idle()

if __name__ == '__main__':
    main()