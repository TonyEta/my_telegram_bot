from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from pyexpat.errors import messages

from chat_gpt.gpt_client import ask_gpt, ask_gpt_talk
from buttons.gpt_buttons import gpt_keyboard
from content.prompts.prompts_for_talk import persons


router = Router()

class GPTStates(StatesGroup):
    waiting_for_question = State()

class ChatStates(StatesGroup):
    waiting_for_message = State()



@router.message(GPTStates.waiting_for_question)
async def user_question_handler(message: Message, state: FSMContext):
    user_text = message.text

    await message.answer("Іде опрацювання питання ...")

    gpt_response = await ask_gpt(user_text)

    await message.answer(
        text=gpt_response,
        reply_markup=gpt_keyboard
    )
    await state.clear()


@router.callback_query(F.data.startswith("person_"))
async def start_person_dialog(callback: CallbackQuery, state: FSMContext):
    person_key = callback.data.split("_")[1]
    prompt = {"role": "user", "content": persons[person_key]}

    await state.update_data(messages=[prompt])
    await state.set_state(ChatStates.waiting_for_message)
    await callback.message.answer("Напиши своє перше повідомлення")










