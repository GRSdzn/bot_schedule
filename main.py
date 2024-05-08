import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from components import help_command, start, website, get_user_text
from utils import get_sticker_id
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN, timeout=120)
dp = Dispatcher(bot)

if __name__ == "__main__":
    dp.register_message_handler(lambda message: start.start(message, dp), commands=['start', 'Start'])
    dp.register_message_handler(lambda message: website.website(message, dp), commands=['rinh', 'RINH', 'Сайт', 'сайт', 'ринх'])
    dp.register_message_handler(lambda message: help_command.help_command(message, dp), commands=['help', 'Help', 'h'])
    dp.register_message_handler(lambda message: get_sticker_id.send_sticker_id(message, dp), content_types=['sticker'])
    dp.register_message_handler(get_user_text.get_user_text)

    executor.start_polling(dp, skip_updates=True)
