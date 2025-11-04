import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher

from handlers import start_help_handlers, main_handlers, state_handlers
from handlers import leisure_handlers, dialog_handlers
from handlers import hr_handlers

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')


async def main():

    bot = Bot(token=TOKEN)

    dp = Dispatcher()

    dp.include_router(start_help_handlers.router)
    dp.include_router(main_handlers.router)
    dp.include_router(state_handlers.router)
    dp.include_router(leisure_handlers.router)
    dp.include_router(dialog_handlers.router)
    dp.include_router(hr_handlers.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
