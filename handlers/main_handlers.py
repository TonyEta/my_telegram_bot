from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile

from buttons.hr_buttons import resume_create_keyboard
from buttons.random_buttons import random_keyboard
from buttons.leisure_buttons import leisure_keyboard
from buttons.talk_buttons import talk_keyboard
from chat_gpt.gpt_client import ask_gpt
from handlers.state_handlers import GPTStates
from content.prompts.prompts_for_random import prompt


router = Router()

@router.callback_query(F.data == "random")
async def cmd_random(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/random-picture.jpg")
    fact = await ask_gpt(prompt)

    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text=fact,
        reply_markup=random_keyboard)


@router.callback_query(F.data == "talk")
async def cmd_talk(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/talk-picture.jpg")
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text="Тут буде діалог з відомою особистістю",
        reply_markup=talk_keyboard)


@router.callback_query(F.data == "gpt")
async def cmd_gpt(callback: CallbackQuery, state: FSMContext):
    photo = FSInputFile("content/pictures/gpt-picture.jpg")
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text="Напишіть своє питання для GPT:")
    await state.set_state(GPTStates.waiting_for_question)


@router.callback_query(F.data == "leisure")
async def cmd_leisure(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/leisure-picture.jpg")
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text="Тут буде рекомендація по вибору фільма",
        reply_markup=leisure_keyboard)


@router.callback_query(F.data == "HR_help")
async def cmd_hr_help(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/hr_help-picture.jpg")
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text="_________________________________",
        reply_markup=resume_create_keyboard)