from aiogram import types
from states.photoState import PhotoData
from loader import dp,bot,db
from aiogram.dispatcher import FSMContext
from keyboards.default.mainKeyboard import menuPython



@dp.message_handler(commands='addphoto',state="*")
async def material_def(message: types.Message):
    # print(1)
    await message.answer("Rasm junating!")
    await PhotoData.photo_link.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=PhotoData.photo_link)
async def forward_photo_to_channel(message: types.Message, state: FSMContext):
    photo = message.photo[-1]  # Get the largest photo
    file_id = photo.file_id  # Get the file ID of the photo
    await state.update_data(
        {"photo_link": file_id}
    )
    await message.answer("Qaysi kategoriyaga tegishli", reply_markup=menuPython)

    await PhotoData.next()


@dp.message_handler(state=PhotoData.photo_category)
async def forward_photo_to_channel(message: types.Message, state: FSMContext):
    text = message.text  # Get the largest photo
    await state.update_data(
        {"photo_category": text}
    )

    data = await state.get_data()
    photo_link = data.get('photo_link')
    photo_category = data.get('photo_category')
    db.add_photo(photo_category=photo_category, photo_link=photo_link)

    await message.answer("Rasm yuklandi")


    await state.finish()
