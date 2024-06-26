"""keyboards modul"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Пермь'), KeyboardButton(text='Прогноз Пермь')]
    ],
    resize_keyboard=True
)