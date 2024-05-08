async def send_sticker_id(message, dp):
    sticker_id = message.sticker.file_id
    await dp.bot.send_message(message.chat.id, f'ID стикера: {sticker_id}')
    # await dp.bot.send_message(message.chat.id, help_command, parse_mode='html')
