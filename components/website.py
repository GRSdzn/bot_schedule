from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components import schedule_data

# 
async def website(message, dp):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Сайт с парами РИНХА", url=schedule_data.URL))
    markup.add(InlineKeyboardButton("Скачать расписание", url=schedule_data.URL))
    await dp.bot.send_message(message.chat.id, 'Пары на сайте', reply_markup=markup)