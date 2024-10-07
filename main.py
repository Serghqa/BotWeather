"""Главный модуль телеграм бота"""

import asyncio
import logging

from logging.config import dictConfig
from aiogram import Bot, Dispatcher
from config import load_config, Config
from handlers.user_handlers import router
from loggers_config import LOGGING_CONFIG

# Загружаем конфиг в переменную config
config: Config = load_config()

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


# Инициализируем бот и диспетчер
bot = Bot(config.tg_bot.token)
dp = Dispatcher()
# Регистрируем роутер в диспечере
dp.include_router(router)


async def main():
    """Старт телеграм бота"""
    # Пропускаем накопившиеся апдейты и запускаем polling
    logger.info('start polling')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
