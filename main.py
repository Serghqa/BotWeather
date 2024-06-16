import asyncio
from aiohttp import ClientSession

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN, KEY_WEATHER


bot = Bot(TOKEN)
dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Perm')]
    ],
    resize_keyboard=True
)


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': KEY_WEATHER}
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            answer = f'{city}: {int(weather_json['main']['temp']-273.15)}'
            return answer


@dp.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer('Погода в Перми', reply_markup=start_kb)


@dp.message(F.text=='Perm')
async def get_weather_answer(message: Message):
    answer = await asyncio.create_task(get_weather('Perm'))
    await message.answer(text=answer)


dp.run_polling(bot)
