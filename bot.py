from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открой мини приложение", web_app={"url": "https://ТВОЙ_СЕРВЕР/mini_app.html"})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Добро пожаловать! Нажмите на кнопку, чтобы открыть мини-приложение:', reply_markup=reply_markup)

def main():
    token = '7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8'

    # Создаем объект Application и передаем токен
    application = Application.builder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()