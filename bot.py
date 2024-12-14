from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import httpx

# Настройка логирования
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Замените на ID вашего канала
CHANNEL_ID = "-1002283526037"  # ИЛИ используйте числовой ID канала

# Указание URL для мини-приложения (можно использовать ngrok URL или IP-адрес)
MINI_APP_URL = "http://127.0.0.1:5000/post"  # или используйте публичный URL, например, через ngrok

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

# Функция публикации контента в канал и мини-приложении
async def post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # Публикация текста
    if message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message.text)

        # Отправляем текст на сервер мини-приложения
        async with httpx.AsyncClient() as client:
            await client.post(MINI_APP_URL, json={"type": "text", "content": message.text})

    # Публикация фото
    if message.photo:
        file_id = message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        photo_url = file.file_path

        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo_url)

        # Отправляем фото на сервер мини-приложения
        async with httpx.AsyncClient() as client:
            await client.post(MINI_APP_URL, json={"type": "photo", "content": photo_url})

    # Публикация видео
    if message.video:
        file_id = message.video.file_id
        file = await context.bot.get_file(file_id)
        video_url = file.file_path

        await context.bot.send_video(chat_id=CHANNEL_ID, video=video_url)

        # Отправляем видео на сервер мини-приложения
        async with httpx.AsyncClient() as client:
            await client.post(MINI_APP_URL, json={"type": "video", "content": video_url})

def main():
    token = '7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8'  # Замените на токен вашего бота

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