from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from chat_gpt.gpt_client import ask_gpt_talk
from handlers.state_handlers import ChatStates
from buttons.talk_buttons import end_keyboard


router = Router()


@router.message(ChatStates.waiting_for_message)
async def chat(message: Message, state: FSMContext):
    user_text = message.text.strip()
    if not user_text:
        await message.answer("Напиши щось")
        return

    data = await state.get_data()
    chat_history = data.get("messages", [])

    chat_history.append({"role": "user", "content": user_text})

    answer = await ask_gpt_talk(chat_history)

    chat_history.append({"role": "assistant", "content": answer})

    await state.update_data(messages=chat_history)
    await message.answer(answer, reply_markup=end_keyboard)