# Telegram Бот для получения расписания пар

## Установка зависимостей
- aiogram -  `pip install aiogram==2.25.2`
- openpyxl - `pip install openpyxl`
- requests - `pip install requests`
- dot-env - `pip install python-dotenv`

## Запуск

- `python main.py`
- Следующим этапом автоматически скачивается расписание

### Данные берутся из .env файла со следующими параметрами
- `TOKEN=` - Токен вашего бота
- `URL=` - адрес для получения расписания
- `STICKERHELLO=` - id необходимого стикера для приветствия
- `STICKERGOODBYE=` - id еобходимого стикера для прощания

P.s id стикера можно получить у самого бота. Для этого написан соответствующий функционал в файле `utils/get_sticker_id.py`
