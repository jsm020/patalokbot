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
            KeyboardButton(text="Космос&Луна"),
            KeyboardButton(text="Небо"),
        ],
        [
            KeyboardButton(text="Дельфин"),
            KeyboardButton(text="Небо & Птицы"),
        ],
                [
            KeyboardButton(text="Дельфин"),
            KeyboardButton(text="Небо & Птицы"),
        ],        [
            KeyboardButton(text="Дельфин"),
            KeyboardButton(text="Небо & Птицы"),
        ],
    ],
    resize_keyboard=True
)