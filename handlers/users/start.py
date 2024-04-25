from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuPython)


list_abs = [2,22,34,46,58,60,72,84]
async def send_photos_range(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_abs[start_index], list_abs[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_abs[start_index], list_abs[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Абстракция & 3d", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range(message, 0, 1, "next_page_2_abs")

@dp.message_handler(commands='next_page_2_abs')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range(message, 1, 2, "next_page_3_abs")

@dp.message_handler(commands='next_page_3_abs')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range(message, 2, 3, "next_page_4_abs")

@dp.message_handler(commands='next_page_4_abs')
async def bot_send_picture_4(message: types.Message):
    await send_photos_range(message, 3, 4, "next_page_5_abs")

@dp.message_handler(commands='next_page_5_abs')
async def bot_send_picture_5(message: types.Message):
    await send_photos_range(message, 4, 5, "next_page_6_abs")

@dp.message_handler(commands='next_page_6_abs')
async def bot_send_picture_6(message: types.Message):
    await send_photos_range(message, 5, 6, "next_page_7_asb")

@dp.message_handler(commands='next_page_7_abs')
async def bot_send_picture_7(message: types.Message):
    await send_last_photos_range(message, 6, 7)



list_vod = [84,90,100,108]
async def send_photos_range(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_vod[start_index], list_vod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_vod[start_index], list_vod[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Водопад", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range(message, 0, 1, "next_page_2_vod")

@dp.message_handler(commands='next_page_2_vod')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range(message, 1, 2, "next_page_3_vod")

@dp.message_handler(commands='next_page_3_vod')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range(message, 2, 3)





@dp.message_handler(text="Город", state="*")
async def bot_send_picture(message:types.Message):
    for nomer in range(109,307):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Детское", state="*")
async def bot_send_picture(message:types.Message):
    for nomer in range(309,443):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Космос & Луна")
async def bot_send_picture(message:types.Message):
    for nomer in range(443,592):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Небо")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)


@dp.message_handler(text="Фрукты и Кофе")
async def bot_send_picture(message:types.Message):
    for nomer in range(660,760):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Птицы")
async def bot_send_picture(message:types.Message):
    for nomer in range(761,792):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Природа")
async def bot_send_picture(message:types.Message):
    for nomer in range(793,875):
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

