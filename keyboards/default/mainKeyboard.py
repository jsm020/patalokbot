from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Абстракция & 3d"),
            KeyboardButton(text="Вода"),
        ],
        [
            KeyboardButton(text="Водопад"),
            KeyboardButton(text="Город"),
        ],
        [
            KeyboardButton(text="Детское"),
            KeyboardButton(text="Исторически"),
        ],
        [
            KeyboardButton(text="Космос & Луна"),
            KeyboardButton(text="Небо"),
        ],
        [
            KeyboardButton(text="Природа"),
            KeyboardButton(text="Птицы"),
        ],
        [
            KeyboardButton(text="Фрукты и Кофе"),
            KeyboardButton(text="ультрафеле"),
        ],
    ],
    resize_keyboard=True
)



