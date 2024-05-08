def get_user_data(message) -> tuple:
    last_name = "" if message.from_user.last_name is None else message.from_user.last_name
    first_name = message.from_user.first_name
    return last_name, first_name
