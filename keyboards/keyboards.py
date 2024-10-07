"""Модуль клавиатур телеграм бота"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Инициализируем билдер погоды
kb_builder_weather = ReplyKeyboardBuilder()

# Создаем кнопки
cur_weather_btn = KeyboardButton(
    text='Текущая погода'
)
forcast_weather_btn = KeyboardButton(
    text='Прогноз погоды'
)

kb_builder_weather.row(cur_weather_btn, forcast_weather_btn)
keyboard_weather: ReplyKeyboardMarkup = kb_builder_weather.as_markup(
    resize_keyboard=True
)
