from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import menuPython
from filters import IsPrivate

from loader import dp,db




@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuPython)







@dp.message_handler(IsPrivate(),text="Птицы")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Птицы")
    for item in photos:
        await message.answer_photo(photo=item[1])
    for nomer in range(761,792):
        photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
        await message.answer_photo(photo=photo_url)


@dp.message_handler(IsPrivate(),text="Исторически")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Исторически")
    for item in photos:
        await message.answer_photo(photo=item[1])
    # for nomer in range(592,659):
    #     photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
    #     await message.answer_photo(photo=photo_url)

@dp.message_handler(IsPrivate(),text="Yльтрафеле")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Yльтрафеле")
    for item in photos:
        await message.answer_photo(photo=item[1])
    # for nomer in range(592,659):
    #     photo_url = f"https://t.me/asafsfbdbfksdbgosgsbgeiw/{nomer}"
    #     await message.answer_photo(photo=photo_url)
@dp.message_handler(IsPrivate(),text="Вода")
async def bot_send_picture(message:types.Message):
    photos = db.select_photo(Photo_category="Вода")
    for item in photos:
        await message.answer_photo(photo=item[1])

# mcjsdnzkncjsd