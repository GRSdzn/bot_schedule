from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand
# from aiogram.types import MenuButtonCommands
from aiogram import Bot

# кнопки вызываемые при старте бота
def create_start_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    today = KeyboardButton('Пары на сегодня')
    tomorrow = KeyboardButton('Пары на завтра')
    week = KeyboardButton('Пары на неделю')

    markup.add(today, tomorrow, week)

    return markup

# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/rinh',
                   description='Сайт с раписанием РИНХ (web / xlsx)'),
        BotCommand(command='/today',
                   description='Пары на сегодня'),
        BotCommand(command='/tomorrow',
                   description='Пары на завтра'),
        BotCommand(command='/week',
                   description='Пары на неделю')
    ]

    await bot.set_my_commands(main_menu_commands)


