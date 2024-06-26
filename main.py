"""main modul"""

import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.handlers import router


load_dotenv()

token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher()
dp.include_router(router)


async def main():
    """start bot"""
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
