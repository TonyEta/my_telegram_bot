from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_end = InlineKeyboardButton(
    text="Закінчити і повернутися до меню",
    callback_data="start"
)

button_books = InlineKeyboardButton(
    text="Яку книгу почитати ?!?",
    callback_data="book"
)

button_films = InlineKeyboardButton(
    text="Який фільм подивитися ?!?",
    callback_data="film"
)

button_music = InlineKeyboardButton(
    text="Яку пісню послухати ?!?",
    callback_data="music"
)

leisure_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_books],
        [button_films],
        [button_music],
        [button_end]
    ]
)

book_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_books],
        [button_end]
    ]
)

film_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_films],
        [button_end]
    ]
)

music_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_music],
        [button_end]
    ]
)