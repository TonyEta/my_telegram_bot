from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Створюємо кілька кнопок
button_random = InlineKeyboardButton(
    text="Випадковий факт",
    callback_data="random"
)

button_help = InlineKeyboardButton(
    text="Допомога",
    callback_data="help"
)

button_talk = InlineKeyboardButton(
    text="Діалог з відомою особистістю",
    callback_data="talk"
)

button_gpt = InlineKeyboardButton(
    text="Запитати ChatGPT",
    callback_data="gpt"
)


button_leisure = InlineKeyboardButton(
    text="Підібрати фільм, книгу, музику",
    callback_data='leisure'
)

button_HR_help = InlineKeyboardButton(
    text="Допомога з оформленням резюме",
    callback_data='HR_help'
)

# Створюємо клавіатуру inline keyboard
start_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_random, button_talk],
        [button_help, button_gpt],
        [button_HR_help, button_leisure],
    ],
    resize_keyboard=True
)
