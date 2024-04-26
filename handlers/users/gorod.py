from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp,db



list_gorod = [109,129,149,169,189,209,229,249,269,289,307]
async def send_photos_range_grd(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_gorod[start_index], list_gorod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_grd(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_gorod[start_index], list_gorod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Город")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Город")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_grd(message, 0, 1, "next_page_2_grd")

@dp.message_handler(commands='next_page_2_grd')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_grd(message, 1, 2, "next_page_3_grd")

@dp.message_handler(commands='next_page_3_grd')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_grd(message, 2, 3, 'next_page_4_grd')

@dp.message_handler(commands='next_page_4_grd')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_grd(message, 3, 4, 'next_page_5_grd')

@dp.message_handler(commands='next_page_5_grd')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_grd(message, 4, 5, 'next_page_6_grd')

@dp.message_handler(commands='next_page_6_grd')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_grd(message, 5, 6, 'next_page_7_grd')

@dp.message_handler(commands='next_page_7_grd')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_grd(message, 6, 7)
