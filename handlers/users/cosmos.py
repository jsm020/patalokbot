from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython
from filters import IsPrivate
from loader import dp,db




list_csc = [443,453,473,500,525,550,575,592]
async def send_photos_range_dst(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_csc[start_index], list_csc[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_dst(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_csc[start_index], list_csc[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(IsPrivate(),text="Космос & Луна")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Космос & Луна")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_dst(message, 0, 1, "next_page_2_csc")

@dp.message_handler(IsPrivate(),commands='next_page_2_csc')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_dst(message, 1, 2, "next_page_3_csc")

@dp.message_handler(IsPrivate(),commands='next_page_3_csc')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 2, 3, 'next_page_4_csc')

@dp.message_handler(IsPrivate(),commands='next_page_4_csc')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 3, 4, 'next_page_5_csc')


@dp.message_handler(IsPrivate(),commands='next_page_5_csc')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 3, 4, 'next_page_6_csc')


@dp.message_handler(IsPrivate(),commands='next_page_6_csc')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_dst(message, 5, 6)
