from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp,db


list_abs = [2,22,34,46,58,60,72,84]
async def send_photos_range_abs(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_abs[start_index], list_abs[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_abs(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_abs[start_index], list_abs[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Абстракция & 3d")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Абстракция & 3d")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_abs(message, 0, 1, "next_page_2_abs")

@dp.message_handler(commands='next_page_2_abs')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_abs(message, 1, 2, "next_page_3_abs")

@dp.message_handler(commands='next_page_3_abs')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_abs(message, 2, 3, "next_page_4_abs")

@dp.message_handler(commands='next_page_4_abs')
async def bot_send_picture_4(message: types.Message):
    await send_photos_range_abs(message, 3, 4, "next_page_5_abs")

@dp.message_handler(commands='next_page_5_abs')
async def bot_send_picture_5(message: types.Message):
    await send_photos_range_abs(message, 4, 5, "next_page_6_abs")

@dp.message_handler(commands='next_page_6_abs')
async def bot_send_picture_6(message: types.Message):
    await send_photos_range_abs(message, 5, 6, "next_page_7_asb")

@dp.message_handler(commands='next_page_7_abs')
async def bot_send_picture_7(message: types.Message):
    await send_last_photos_range_abs(message, 6, 7)
