from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_guido = InlineKeyboardButton(
    text="Гвідо ван Россум",
    callback_data="person_guido"
)

button_garri = InlineKeyboardButton(
    text="Гаррі Стайлз",
    callback_data="person_garri"
)

button_dalay_lama = InlineKeyboardButton(
    text="Далай-Лама",
    callback_data="person_dalay"
)

button_end = InlineKeyboardButton(
    text="Закінчити розмову",
    callback_data="start"
)
talk_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_guido],
        [button_garri],
        [button_dalay_lama]
    ]
)

end_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_end]
    ]
)