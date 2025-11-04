from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_create_resume = InlineKeyboardButton(
    text="Натисність щоб створити резюме",
    callback_data="resume"
)

button_end = InlineKeyboardButton(
    text="Закінчити і повернутися до меню",
    callback_data="start"
)


resume_create_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_create_resume],
                     [button_end]]
)