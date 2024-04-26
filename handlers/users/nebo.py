from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp,db


list_nb = [592,600,625,650,659]
async def send_photos_range_dst(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_nb[start_index], list_nb[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_dst(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_nb[start_index], list_nb[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Небо")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Небо")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_dst(message, 0, 1, "next_page_2_nb")

@dp.message_handler(commands='next_page_2_nb')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_dst(message, 1, 2, "next_page_3_nb")

@dp.message_handler(commands='next_page_3_nb')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 2, 3, 'next_page_4_nb')

@dp.message_handler(commands='next_page_4_nb')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_dst(message, 3, 4)
