from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython

from loader import dp




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

@dp.message_handler(text="Абстракция & 3d", state="*")
async def bot_send_picture(message: types.Message):
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

# ____________________________________________________________

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

@dp.message_handler(text="Водопад", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range_vod(message, 0, 1, "next_page_2_vod")

@dp.message_handler(commands='next_page_2_vod')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_vod(message, 1, 2, "next_page_3_vod")

@dp.message_handler(commands='next_page_3_vod')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_vod(message, 2, 3)


# ____________________________________________________________

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

@dp.message_handler(text="Город", state="*")
async def bot_send_picture(message: types.Message):
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

# _____________________________________________________



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

@dp.message_handler(text="Детское", state="*")
async def bot_send_picture(message: types.Message):
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
# _______________________________________________________


list_ln = [443,463,483,503,523,543,563,592]
async def send_photos_range_ln(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_ln[start_index], list_ln[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_ln(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_ln[start_index], list_ln[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Космос & Луна", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range_ln(message, 0, 1, "next_page_2_ln")

@dp.message_handler(commands='next_page_2_ln')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_ln(message, 1, 2, "next_page_3_ln")

@dp.message_handler(commands='next_page_3_ln')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_ln(message, 2, 3, 'next_page_4_ln')

@dp.message_handler(commands='next_page_4_ln')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_ln(message, 3, 4)
# ________________________________________________________

list_nb = [592,612,622,659]
async def send_photos_range_nb(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_nb[start_index], list_nb[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_nb(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_nb[start_index], list_nb[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(commands='next_page_2_ln')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_nb(message, 0, 1, "next_page_2_nb")

@dp.message_handler(commands='next_page_2_ln')
async def bot_send_picture_2(message: types.Message):
    await send_photos_range_nb(message, 1, 2, "next_page_3_nb")



@dp.message_handler(commands='next_page_3_nb')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_nb(message, 2, 3, 'next_page_4_nb')

@dp.message_handler(commands='next_page_3_nb')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_nb(message, 3, 4)
# ___________________________________________________________

list_ft = [659,679,699,719,739,760]
async def send_photos_range_ft(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_ft[start_index], list_ft[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_ft(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_ft[start_index], list_ft[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Фрукты и Кофе", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range_ft(message, 0, 1, "next_page_2_ft")
    
@dp.message_handler(commands='next_page_2_nb')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_ft(message, 1, 2, 'next_page_3_nb')

@dp.message_handler(commands='next_page_3_nb')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_ft(message, 3, 4)
# _________________________________________________

list_pt = [761,781,792]
async def send_photos_range_pt(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_pt[start_index], list_pt[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_pt(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_pt[start_index], list_pt[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Птицы", state="*")
async def bot_send_picture(message: types.Message):
    await send_last_photos_range_pt(message, 0, 1, "next_page_2_pt")
    
@dp.message_handler(commands='next_page_2_nb')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_ft(message, 1,2)
# ________________________________________________________________________________

list_pr = [792,812,822,842,862,875]
async def send_photos_range_pr(message: types.Message, start_index: int, end_index: int, next_command: str):
    for nomer in range(list_pr[start_index], list_pr[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
    await message.answer(f"Keyingisi uchun /{next_command}")

async def send_last_photos_range_pr(message: types.Message, start_index: int, end_index: int):
    for nomer in range(list_pr[start_index], list_pr[end_index]):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)

@dp.message_handler(text="Природа", state="*")
async def bot_send_picture(message: types.Message):
    await send_photos_range_pr(message, 0, 1, "next_page_2_pr")
    
@dp.message_handler(commands='next_page_2_pr')
async def bot_send_picture_3(message: types.Message):
    await send_photos_range_pr(message, 1, 2, 'next_page_3_pr')

@dp.message_handler(commands='next_page_3_pr')
async def bot_send_picture_3(message: types.Message):
    await send_last_photos_range_pr(message, 3, 4)
# _________________________________________________


@dp.message_handler(text="Исторически")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)
# _______________________________________________________
@dp.message_handler(text="ультрафеле")
async def bot_send_picture(message:types.Message):
    for nomer in range(592,659):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)


# mcjsdnzkncjsd