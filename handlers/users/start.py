from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp,db




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuPython)


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

@dp.message_handler(text="Водопад")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Водопад")
    for item in photos:
        await message.answer_photo(photo=item[1])

    await send_photos_range_vod(message, 0, 1, "next_page_2_vod")

@dp.message_handler(commands='next_page_2_vod')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_vod(message, 1, 2, "next_page_3_vod")

@dp.message_handler(commands='next_page_3_vod')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_vod(message, 2, 3)




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





list_dst = [309,329,349,369,389,409,429,443]
async def send_photos_range_dst(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_dst[start_index], list_dst[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_dst(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_dst[start_index], list_dst[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Детское")
async def bot_send_picture(message: types.Message):
    photos = db.select_photo(Photo_category="Детское")
    for item in photos:
        await message.answer_photo(photo=item[1])
    await send_photos_range_dst(message, 0, 1, "next_page_2_dst")

@dp.message_handler(commands='next_page_2_dst')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_dst(message, 1, 2, "next_page_3_dst")

@dp.message_handler(commands='next_page_3_dst')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_dst(message, 2, 3, 'next_page_4_dst')

@dp.message_handler(commands='next_page_4_dst')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_dst(message, 3, 4)


@dp.message_handler(text="Космос & Луна")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Космос & Луна")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(443,592):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Небо")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Небо")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)


@dp.message_handler(text="Фрукты и Кофе")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Фрукты и Кофе")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(660,760):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Птицы")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Птицы")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(761,792):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Природа")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Природа")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(793,875):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Исторически")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Исторически")
    for item in photos:
        await message.answer_photo(photo=item[1])
    # for nomer in range(592,659):
    #     photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
    #     await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Yльтрафеле")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Yльтрафеле")
    for item in photos:
        await message.answer_photo(photo=item[1])
    # for nomer in range(592,659):
    #     photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
    #     await message.answer_photo(photo=photo_url)
@dp.message_handler(text="Вода")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Вода")
    for item in photos:
        await message.answer_photo(photo=item[1])

# mcjsdnzkncjsd