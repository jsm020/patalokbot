from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вода"),
            KeyboardButton(text="Водопад"),
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
            KeyboardButton(text="Фрукты + 3d"),
            KeyboardButton(text="Птицы"),
        ],
        [
            KeyboardButton(text="Луна & Небо"),
            KeyboardButton(text="Природа"),
        ],
        [
            KeyboardButton(text="Исторически"),
            KeyboardButton(text="ультрафеле"),
        ],
    ],
    resize_keyboard=True
)


