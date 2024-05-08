from aiogram.types import InputFile
from index import bot, dp
from components import schedule_data, help_command
from components.user_data import get_user_data
import os
from dotenv import load_dotenv

load_dotenv()
sticker_goodbye_id = os.getenv("STICKERGOODBYE")
sticker_hello_id = os.getenv("STICKERHELLO")

@dp.message_handler()
async def get_user_text(message):
    last_name, first_name = get_user_data(message)  # получаем данные пользователя
    text = message.text.lower()

    if text in ["привет", "hi"]:
        await bot.send_message(message.chat.id, f'Привет, {first_name} {last_name}!')
        await bot.send_sticker(message.chat.id, sticker_hello_id)

    elif text == "пока":
        await bot.send_message(message.chat.id, 'Ну, пока 😔')
        await bot.send_sticker(message.chat.id, sticker_goodbye_id)

    elif text in ["пары на сегодня", "/today", "сегодня", "пары", "ща"]:
        schedule = schedule_data.get_today_schedule()
        await bot.send_message(message.chat.id, schedule, parse_mode='html')

    elif text in ["пары на завтра", "/tomorrow", "завтра"]:
        schedule = schedule_data.get_tomorrow_schedule()
        await bot.send_message(message.chat.id, schedule, parse_mode='html')

    elif text in ["пары на неделю", "/week", "неделя"]:
        schedule = schedule_data.get_week_schedule()
        await bot.send_message(message.chat.id, '<strong>Вот расписание на неделю</strong>\n\n\n' + schedule,
                               parse_mode='html')

    elif text == "спасибо":
        await bot.send_message(message.chat.id, 'Обращайся! Рад помочь в любое время! (P.s пока не упал сервер)')

    elif text == "help":
        await bot.send_message(message.chat.id, help_command)
    else:
        await bot.send_message(message.chat.id, f'Я не понимаю, что вы мне написали 😕')
