from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile

from buttons.help_buttons import help_inline_keyboard
from buttons.start_buttons import start_inline_keyboard


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    photo = FSInputFile("content/pictures/main-picture.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Оберіть дію нижче",
        reply_markup=start_inline_keyboard
    )


@router.callback_query(F.data == "help")
async def cmd_help(callback: CallbackQuery):
    await callback.message.answer(text="Bot inf:",
        reply_markup=help_inline_keyboard)

@router.callback_query(F.data == "start")
async def cmd_back_start(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/main-picture.jpg")
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text="Оберіть дію нижче:",
        reply_markup=start_inline_keyboard)

