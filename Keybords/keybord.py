from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder,InlineKeyboardMarkup, KeyboardBuilder
from aiogram.filters.callback_data import CallbackData, CallbackQuery
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton
)

builder =  ReplyKeyboardMarkup(keyboard=[
        [
           KeyboardButton(text="/settings", callback_data="settings")
        ],
        [
            KeyboardButton(text="/generate", callback_data="generate")
        ]
    ],
    resize_keyboard= True
)



Razmer = KeyboardBuilder(button_type=InlineKeyboardButton, markup=[
    [
        InlineKeyboardButton(text="little", callback_data= "little")
    ],
    [
        InlineKeyboardButton(text="middle", callback_data= "middle")
    ],
    [
        InlineKeyboardButton(text="big", callback_data= "big")
    ]
])
markup = InlineKeyboardMarkup(inline_keyboard=Razmer.export())
