async def help_command(message, dp):
    help_command = f"<u>Вот список доступных команд:</u>\n\n" \
                f"<b>/today | 'ща' | 'сегодня' | 'пары(сегодня)'</b> - Отображение пар на сегодня\n\n" \
                f"<b>/tomorrow | 'завтра' | 'пары(завтра)'</b> - Отображение пар на завтра\n\n" \
                f"<b>/week | 'неделя' | 'пары(неделя)'</b> - Отображение пар на неделю\n\n" \
                f"<b>'/rinh' | '/RINH' | '/Сайт' | '/сайт' | '/ринх'</b> - Отображение пар на неделю\n\n"

    await dp.bot.send_message(message.chat.id, help_command, parse_mode='html')