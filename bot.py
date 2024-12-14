from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Замените на ID вашего канала
CHANNEL_ID = "-1002283526037"  # Используй числовой ID канала

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открой мини приложение", web_app={"url": "https://lebedevdsn.github.io/tutsTGbots"})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Добро пожаловать! Нажмите на кнопку, чтобы узнать что у Маришки в попе сегодня:', 
        reply_markup=reply_markup
    )

# Функция для обработки текстовых сообщений и публикации их в канал
async def post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text  # Получаем текст сообщения от пользователя

    try:
        # Отправляем текст в канал (без имени пользователя)
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=user_message
        )
        # Подтверждаем пользователю, что сообщение отправлено
        await update.message.reply_text("Ваше сообщение отправлено в канал!")
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения в канал: {e}")
        await update.message.reply_text("Не удалось отправить сообщение в канал. Проверьте настройки.")

def main():
    token = '7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8'  # Токен вашего бота

    # Создаем объект Application и передаем токен
    application = Application.builder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, post_to_channel))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

