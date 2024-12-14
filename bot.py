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

# Функция для обработки текста и публикации в канал
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text  # Получаем текст сообщения

    try:
        # Отправляем текст в канал
        await context.bot.send_message(chat_id=CHANNEL_ID, text=user_message)
        await update.message.reply_text("Ваше текстовое сообщение отправлено в канал!")
    except Exception as e:
        logging.error(f"Ошибка отправки текста в канал: {e}")
        await update.message.reply_text("Не удалось отправить текстовое сообщение в канал.")

# Функция для обработки фото и публикации в канал
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  # Берем самое большое качество фото
    caption = update.message.caption  # Текст, прикрепленный к фото (если есть)

    try:
        # Отправляем фото в канал
        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo.file_id, caption=caption)
        await update.message.reply_text("Ваше фото отправлено в канал!")
    except Exception as e:
        logging.error(f"Ошибка отправки фото в канал: {e}")
        await update.message.reply_text("Не удалось отправить фото в канал.")

# Функция для обработки видео и публикации в канал
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video  # Получаем видео
    caption = update.message.caption  # Текст, прикрепленный к видео (если есть)

    try:
        # Отправляем видео в канал
        await context.bot.send_video(chat_id=CHANNEL_ID, video=video.file_id, caption=caption)
        await update.message.reply_text("Ваше видео отправлено в канал!")
    except Exception as e:
        logging.error(f"Ошибка отправки видео в канал: {e}")
        await update.message.reply_text("Не удалось отправить видео в канал.")

def main():
    token = '7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8'  # Токен вашего бота

    # Создаем объект Application и передаем токен
    application = Application.builder().token(token).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Обработчик фото
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Обработчик видео
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
