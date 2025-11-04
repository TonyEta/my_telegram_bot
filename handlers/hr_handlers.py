from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from chat_gpt.gpt_client import ask_gpt_talk
from content.prompts.prompts_for_resume import prompt_for_resume
from buttons.hr_buttons import resume_create_keyboard
router = Router()


class ResumeStates(StatesGroup):
    name = State()
    age = State()
    contacts = State()
    education = State()
    skills = State()
    languages = State()
    motivation = State()

@router.callback_query(F.data == "resume")
async def start_resume(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ResumeStates.name)
    await callback.message.answer("Напиши своє повне Ім'я")

@router.message(ResumeStates.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ResumeStates.age)
    await message.answer("Вкажи свій вік")

@router.message(ResumeStates.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(ResumeStates.contacts)
    await message.answer("Вкажи свої контактні дані (телефон, email)")

@router.message(ResumeStates.contacts)
async def get_contacts(message: Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await state.set_state(ResumeStates.education)
    await message.answer("Напиши інформацію про освіту")

@router.message(ResumeStates.education)
async def get_education(message: Message, state: FSMContext):
    await state.update_data(education=message.text)
    await state.set_state(ResumeStates.skills)
    await message.answer("Якими технологіями ти володієш")

@router.message(ResumeStates.skills)
async def get_skills(message: Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await state.set_state(ResumeStates.languages)
    await message.answer("Якими мовами ти володієш")

@router.message(ResumeStates.languages)
async def get_language(message: Message, state: FSMContext):
    await state.update_data(languages=message.text)
    await state.set_state(ResumeStates.motivation)
    await message.answer("Напиши причину, чому мають взяти особисто тебе")

@router.message(ResumeStates.motivation)
async def get_motivation(message: Message, state: FSMContext):
    await state.update_data(motivation=message.text)
    data = await state.get_data()

    user_resume_text = (
        f"Ім’я та вік: {data.get('name')}, {data.get('age')}\n"
        f"Контакти: {data.get('contacts')}\n"
        f"Освіта: {data.get('education')}\n"
        f"Навички: {data.get('skills')}\n"
        f"Мови: {data.get('languages')}\n"
        f"Мотивація: {data.get('motivation')}\n"
    )

    chat_history = [
        {
            "role": "system",
            "content": prompt_for_resume
        },
        {
            "role": "user",
            "content": (
                f"Склади резюме з таких даних:\n{user_resume_text}"
            )
        }
    ]

    resume = await ask_gpt_talk(chat_history)
    await message.answer(resume, reply_markup=resume_create_keyboard)
    await state.clear()
