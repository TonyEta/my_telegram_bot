from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_random = InlineKeyboardButton(
    text="/random - випадковий факт",
    callback_data="random"
)

button_talk = InlineKeyboardButton(
    text="/talk - діалог з відомою особистістю",
    callback_data="talk"
)

button_gpt = InlineKeyboardButton(
    text="/gpt - запитати ChatGPT",
    callback_data="gpt"
)

button_leisure = InlineKeyboardButton(
    text="/leisure - рекомендація книги, фільму, пісні",
    callback_data='leisure'
)

button_HR_help = InlineKeyboardButton(
    text="/hr_help - допомога з оформленням резюме",
    callback_data="HR_help"
)

button_back_to_menu = InlineKeyboardButton(
    text="/start - повернутися до основного меню",
    callback_data="start"
)

help_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_random],
        [button_talk],
        [button_gpt],
        [button_leisure],
        [button_HR_help],
        [button_back_to_menu]
    ],
    resize_keyboard=True
)