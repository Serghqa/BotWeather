"""handler modul"""

import asyncio
import os
import time

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiohttp import ClientSession
from dotenv import load_dotenv
from keyboards.keyboards import start_kb


load_dotenv()
key_weather = os.getenv('KEY_WEATHER')
router = Router()

coord_perm = {'lon': 56.2855, 'lat': 58.0174}


def get_current_weather(weather: dict) -> str:
    """return string current weather"""
    temp = int(weather['main']['temp'])
    temp_feel = int(weather['main']['feels_like'])
    press = weather['main']['pressure']
    humidity = weather['main']['humidity']
    answer = f'Температура в Перми {temp}\nПо ощущениям {temp_feel}\n'\
        f'Давление {press}\nВлажность {humidity}'
    return answer


def get_forcast_weather(weather: dict) -> str:
    """return string forcast weather"""
    dates = [time.strftime('%B %d %Y', time.gmtime(float(date['dt']))) for date in weather['list']]
    answer = '\n'.join(dates)
    return answer


async def get_weather(forcast=False) -> str:
    """return weather"""
    async with ClientSession() as session:
        current_url = 'http://api.openweathermap.org/data/2.5/weather'
        forcast_url = 'http://api.openweathermap.org/data/2.5/forecast'
        params = {'lon': coord_perm['lon'], 'lat': coord_perm['lat'],
                  'appid': key_weather, 'units': 'metric'}
        url = current_url if forcast else forcast_url
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            if forcast:
                return get_current_weather(weather_json)
            return get_forcast_weather(weather_json)


@router.message(CommandStart())
async def cmd_start(message: Message):
    """answer bot for user start"""
    await message.answer('Погода в Перми', reply_markup=start_kb)


@router.message(F.text == 'Пермь')
async def get_weather_answer(message: Message):
    """answer bot for user Пермь"""
    answer = await asyncio.create_task(get_weather(True))
    await message.answer(text=answer)


@router.message(F.text == 'Прогноз Пермь')
async def get_forcast_weather_answer(message: Message):
    """answer bot for user Прогноз Пермь"""
    answer = await asyncio.create_task(get_weather())
    await message.answer(text=answer)
