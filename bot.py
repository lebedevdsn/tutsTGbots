from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F
from aiogram.filters import Command
from aiogram.webhook.aiohttp import WebhookResponse

API_TOKEN = "7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Нажми на кнопку, чтобы открыть Mini App:")

if __name__ == "__main__":
    dp.run_polling()




# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
# from aiogram.utils import executor

# # Токен от BotFather
# API_TOKEN = "7758221545:AAF5qzVWzBqB_eqIitAlADFR3_di2jBFGC8"  # Замени на свой токен

# # Инициализация бота
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# # Обработчик команды /start
# @dp.message_handler(commands=["start"])
# async def send_welcome(message: types.Message):
#     # Создание кнопки с Mini App
#     web_app = WebAppInfo(url="https://lebedevdsn.github.io/tutsTGbots")  # Замени на свой URL
#     keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Открыть Mini App", web_app=web_app))
    
#     # Отправка сообщения с кнопкой
#     await message.answer("Привет! Нажми на кнопку, чтобы открыть Mini App:", reply_markup=keyboard)

# # Запуск бота
# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)