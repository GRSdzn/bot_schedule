from components.user_data import get_user_data
from utils.buttons import create_start_buttons, set_main_menu

async def start(message, dp):
    last_name, first_name = get_user_data(message)
    msg = f'Привет, <b>{first_name}</b> {last_name}. Для получения списка команд, введите /help или /h'
    markup = create_start_buttons()
    await dp.bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')
    await set_main_menu(dp.bot)