"""Модуль хэндлеров телеграм бота"""

import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.keyboards import keyboard_weather
from functions.services import get_weather


router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: Message):
    """запуск бота. Инициализация кнопок"""

    logger.info('нажата кнопка </start>')
    await message.answer('Точная погода в Перми',
                         reply_markup=keyboard_weather)


@router.message(F.text == 'Текущая погода')
async def get_weather_answer(message: Message):
    """Получить текущие данные о погоде"""

    logger.info('нажата кнопка <Текущая погода>')
    answer = await get_weather()
    await message.answer(text=answer)


@router.message(F.text == 'Прогноз погоды')
async def get_forcast_weather_answer(message: Message):
    """Получить данные о погоде на 5 дней"""

    logger.info('нажата кнопка <Прогноз погоды>')
    answer = await get_weather(True)
    await message.answer(text=answer)


@router.message()
async def print_update(message: Message):
    """Отладка бота"""

    logger.info('ответ бота на неопознанную команду, отладка...')
    await message.answer(text='...')
