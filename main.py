import asyncio
from aiohttp import ClientSession
from api import api


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': api}
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {int(weather_json['main']['temp']-273.15)}')


async def main(city):
    task = asyncio.create_task(get_weather(city))
    await task


asyncio.run(main('Perm'))