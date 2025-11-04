from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_end = InlineKeyboardButton(
    text="Закінчити і повернутися до меню",
    callback_data="start"
)

button_gpt = InlineKeyboardButton(
    text="Ще одне питання",
    callback_data="gpt"
)

gpt_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_gpt, button_end]
    ]
)