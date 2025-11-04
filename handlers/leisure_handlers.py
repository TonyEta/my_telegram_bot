from aiogram import Router, F
from aiogram.types import CallbackQuery
from chat_gpt.gpt_client import ask_gpt
from buttons.leisure_buttons import book_keyboard, film_keyboard, music_keyboard

router = Router()

@router.callback_query(F.data == "book")
async def choose_book(callback: CallbackQuery):
    prompt = "Дай рекомендацію яку книгу почитати на дозвіллі"
    book = await ask_gpt(prompt)

    await callback.message.answer(text=book,
        reply_markup=book_keyboard)


@router.callback_query(F.data == "film")
async def choose_film(callback: CallbackQuery):
    prompt = "Дай рекомендацію який фільм подивитися на дозвіллі"
    film = await ask_gpt(prompt)

    await callback.message.answer(text=film,
        reply_markup=film_keyboard)


@router.callback_query(F.data == "music")
async def choose_music(callback: CallbackQuery):
    prompt = "Дай рекомендацію яку українську народну пісню можна послухати на дозвіллі на дозвіллі"
    music = await ask_gpt(prompt)

    await callback.message.answer(text=music,
        reply_markup=music_keyboard)