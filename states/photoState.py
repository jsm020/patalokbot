from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PhotoData(StatesGroup):
    photo_link = State() 
    photo_category = State() 
