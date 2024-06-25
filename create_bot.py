import os

import asyncio

from aiohttp import ClientSession

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
key_weather = os.getenv('KEY_WEATHER')

bot = Bot(token)
dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Perm')]
    ],
    resize_keyboard=True
)


async def get_weather(city):
    async with ClientSession() as session:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': key_weather, 'units': 'metric'}
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            temp = f'{city}: {int(weather_json['main']['temp'])}'
            temp_feel = f'{int(weather_json['main']['feels_like'])}'
            press = f'{int(weather_json['main']['pressure'])}'
            humidity = f'{int(weather_json['main']['humidity'])}'
            answer = f'Температура {temp}\nПо ощущениям {temp_feel}\n'\
                f'Давление {press}\nВлажность {humidity}'

            return answer


@dp.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer('Погода в Перми', reply_markup=start_kb)


@dp.message(F.text=='Perm')
async def get_weather_answer(message: Message):
    answer = await asyncio.create_task(get_weather('Perm'))
    await message.answer(text=answer)


dp.run_polling(bot)
