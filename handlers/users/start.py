from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuPython)



@dp.message_handler(text="Абстракция и 3d")
async def bot_send_picture(message:types.Message):
    for nomer in range(2,84):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Водопад")
async def bot_send_picture(message:types.Message):
    for nomer in range(85,108):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Город")
async def bot_send_picture(message:types.Message):
    for nomer in range(109,307):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Детское")
async def bot_send_picture(message:types.Message):
    for nomer in range(309,442):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Космос & Луна")
async def bot_send_picture(message:types.Message):
    for nomer in range(443,591):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Небо")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)


@dp.message_handler(text="Фрукты и Кофе")
async def bot_send_picture(message:types.Message):
    for nomer in range(660,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Птицы")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Природа")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Исторически")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="ультрафеле")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

