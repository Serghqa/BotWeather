"""Функциональный модуль телеграм бота"""

import logging

from aiohttp import ClientSession
from config import Config, load_config
from locations.locations import locations


geocoding = 'http://api.openweathermap.org/geo/1.0/reverse'
url_weather = {
    'current_url': 'http://api.openweathermap.org/data/2.5/weather',
    'forecast_url': 'http://api.openweathermap.org/data/2.5/forecast'
    }

# Загружаем конфиг в переменную config
config: Config = load_config()
# Получаем ключ для запроса погоды на сервере
key_weather: str = config.url_weather.url
logger = logging.getLogger(__name__)


def process_weather(weather: dict, forecast=False) -> str:
    """Обработка ответа от сервера с фильтром"""

    if not forecast:
        # Получаем текущую погоду
        return get_current_weather(weather)
    # Получаем прогноз погоды с шагом 3 часа на 5 дней
    return get_forecast_weather(weather)


def get_forecast_weather(weather: dict) -> str:
    """Обработка данных о погоде из ответа от сервера
       на 5 дней с шагом 3 часа"""

    tmp = {}
    answer = []
    for data in weather['list']:
        date_ = data['dt_txt'][:10]
        time_ = data['dt_txt'][11:16]
        temp_ = get_current_weather(data)
        tmp.setdefault(date_, []).append(f'{time_} -> {temp_}')
    for date, temps in tmp.items():
        temps = '\n'.join(temps)
        line = f'<<<{date}>>>\n{temps}\n{'*'*10}'
        answer.append(line)
    return '\n'.join(answer)


def get_current_weather(weather: dict) -> str:
    """Обработка данных о текущей погоде из ответа от сервера"""

    temp = round(float(weather['main']['temp']))  # Темп-ра Целсий
    return f'Температура {temp}'


def get_url(forecast=False) -> str:
    """Выбор url-запроса
       forecast==True -> прогноз погоды на 5 дней с шагом 3 часа
       forecast==False -> текущий прогноз погоды"""

    return url_weather['current_url'] \
        if not forecast else url_weather['forecast_url']


async def get_weather(forecast=False) -> str:
    """Полученить данные о погоде"""

    async with ClientSession() as session:
        lon, lat = locations['perm']
        params = {'lon': lon,
                  'lat': lat,
                  'appid': key_weather,
                  'units': 'metric'}
        url = get_url(forecast)
        logger.info('получили url = %s', url)
        logger.info('lon=%s, lat=%s', lon, lat)
        async with session.get(url=url, params=params) as response:
            logger.info('статус код запроса == %s', response.status)
            weather_json = await response.json()
            logger.info(weather_json)
            return process_weather(weather_json, forecast)
