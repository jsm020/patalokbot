from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вода"),
            KeyboardButton(text="Водопад"),
            KeyboardButton(text="Абстракция & 3d"),
        ],
        [
            KeyboardButton(text="Город"),
            KeyboardButton(text="Детское"),
        ],
        [
            KeyboardButton(text="Космос & Луна"),
            KeyboardButton(text="Небо"),
        ],
        [
            KeyboardButton(text="Фрукты и Кофе"),
            KeyboardButton(text="Птицы"),
        ],
        [
            KeyboardButton(text="Природа"),
        ],
        [
            KeyboardButton(text="Исторически"),
            KeyboardButton(text="ультрафеле"),
        ],
    ],
    resize_keyboard=True
)


