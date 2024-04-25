from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuPython)


list = [2,22,34,46,58,60,72,84]
async def send_photos_range(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list[start_index], list[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

<<<<<<< HEAD
async def send_last_photos_range(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list[start_index], list[end_index]):
=======
@dp.message_handler(text="Абстракция и 3d")
async def bot_send_picture(message:types.Message):
    for nomer in range(2,84):
>>>>>>> a0ff6db3b28ee5eda705784b37002b55ef03e2f8
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Вода", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range(message, 0, 1, "next_page_2_voda")

@dp.message_handler(commands='next_page_2_voda')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range(message, 1, 2, "next_page_3_voda")

@dp.message_handler(commands='next_page_3_voda')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range(message, 2, 3, "next_page_4_voda")

@dp.message_handler(commands='next_page_4_voda')
async def bot_send_picture_4(message: types.Message):
    await send_photos_range(message, 3, 4, "next_page_5_voda")

@dp.message_handler(commands='next_page_5_voda')
async def bot_send_picture_5(message: types.Message):
    await send_photos_range(message, 4, 5, "next_page_6_voda")

@dp.message_handler(commands='next_page_6_voda')
async def bot_send_picture_6(message: types.Message):
    await send_photos_range(message, 5, 6, "next_page_7_voda")

@dp.message_handler(commands='next_page_7_voda')
async def bot_send_picture_7(message: types.Message):
    await send_last_photos_range(message, 6, 7)


@dp.message_handler(text="Водопад", state="*")
async def bot_send_picture(message:types.Message):
    for nomer in range(85,108):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Город", state="*")
async def bot_send_picture(message:types.Message):
    for nomer in range(109,307):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Детское", state="*")
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

