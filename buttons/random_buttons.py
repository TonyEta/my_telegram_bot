from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_end = InlineKeyboardButton(
    text="Закінчити і повернутися до меню",
    callback_data="start"
)

button_random = InlineKeyboardButton(
    text="Ще один випадковий факт",
    callback_data="random"
)

random_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_random, button_end]
    ]
)