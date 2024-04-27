from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython
from filters import IsPrivate
from loader import dp,db


list_vod = [84,90,100,108]
async def send_photos_range_vod(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_vod[start_index], list_vod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_vod(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_vod[start_index], list_vod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(IsPrivate(),text="Водопад")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Водопад")
    for item in photos:
        await message.answer_photo(photo=item[1])

    await send_photos_range_vod(message, 0, 1, "next_page_2_vod")

@dp.message_handler(IsPrivate(),commands='next_page_2_vod')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_vod(message, 1, 2, "next_page_3_vod")

@dp.message_handler(IsPrivate(),commands='next_page_3_vod')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_vod(message, 2, 3)
