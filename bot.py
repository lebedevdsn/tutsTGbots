from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import requests

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
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
        'Добро пожаловать! Нажмите на кнопку, чтобы узнать что у Маришки в попе fсегодня:', 
        reply_markup=reply_markup
    )

# Функция публикации контента в канал и мини-приложении
async def post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    logging.debug(f"Received message: {message.text}")  # Логируем входящее сообщение

    # Публикация текста
    if message.text:
        logging.debug(f"Posting text to channel: {message.text}")
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message.text)

        # Отправляем текст на сервер мини-приложения
        try:
            response = requests.post("http://127.0.0.1:5000/post", json={"type": "text", "content": message.text})
            logging.debug(f"Response from mini app: {response.status_code} - {response.text}")
        except Exception as e:
            logging.error(f"Error posting to mini app: {e}")

    # Публикация фото
    if message.photo:
        file_id = message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        photo_url = file.file_path
        logging.debug(f"Posting photo to channel: {photo_url}")

        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo_url)

        # Отправляем фото на сервер мини-приложения
        try:
            response = requests.post("http://127.0.0.1:5000/post", json={"type": "photo", "content": photo_url})
            logging.debug(f"Response from mini app: {response.status_code} - {response.text}")
        except Exception as e:
            logging.error(f"Error posting to mini app: {e}")

    # Публикация видео
    if message.video:
        file_id = message.video.file_id
        file = await context.bot.get_file(file_id)
        video_url = file.file_path
        logging.debug(f"Posting video to channel: {video_url}")

        await context.bot.send_video(chat_id=CHANNEL_ID, video=video_url)

        # Отправляем видео на сервер мини-приложения
        try:
            response = requests.post("http://127.0.0.1:5000/post", json={"type": "video", "content": video_url})
            logging.debug(f"Response from mini app: {response.status_code} - {response.text}")
        except Exception as e:
            logging.error(f"Error posting to mini app: {e}")

# Основная функция
def main():
    token = '7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8'  # Токен вашего бота

    # Создаем объект Application и передаем токен
    application = Application.builder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, post_to_channel))

    # Обработчик фото
    application.add_handler(MessageHandler(filters.PHOTO, post_to_channel))

    # Обработчик видео
    application.add_handler(MessageHandler(filters.VIDEO, post_to_channel))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()