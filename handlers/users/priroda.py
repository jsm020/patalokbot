from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp,db


list_pr = [793,800,825,850,875]
async def send_photos_range_dst(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_pr[start_index], list_pr[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_dst(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_pr[start_index], list_pr[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Природа")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Природа")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_dst(message, 0, 1, "next_page_2_pr")

@dp.message_handler(commands='next_page_2_pr')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_dst(message, 1, 2, "next_page_3_pr")

@dp.message_handler(commands='next_page_3_pr')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 2, 3, 'next_page_4_pr')

@dp.message_handler(commands='next_page_4_pr')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_dst(message, 3, 4)
