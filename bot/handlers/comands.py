import asyncio
from aiogram import F
# from datetime import datetime
from aiogram import Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
# from handlers.logic import sqlite3
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):

    text = (
        "Привіт я був створений для того аби допомогти знайти тобі потрібний фільм."
        )
    text1 = (
        "будьласка оберіть потрбіну вам дію"
        )
    
    # Создание кнопок для обычной клавиатуры
    kb = [
        [KeyboardButton(text="Почати пошук"), KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text)
    await asyncio.sleep(1)
    await message.answer(text1, reply_markup=keyboard)

@router.message(lambda message: message.text == 'Почати пошук')
async def cmd_poshuk_films(message: types.Message):
    """Організація пошуку фільма за критеріями"""
    kb = [
        [KeyboardButton(text="Новинки"), KeyboardButton(text="Меню")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    text1 = str("Напишіть будьласка Рік фільму якого ви хочете знайти та жанр")
    text2 = str("\nНаприклад 2012 драма")
    text3 = str("Також ви можете повернутися в меню або натиснувши кнопку новинки моментально ортимати список свіжих фільмів")
    full_text = text1+text2
    await asyncio.sleep(1)
    await message.reply(full_text, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer(text3, reply_markup=keyboard)







@router.message(lambda message: message.text == 'Допомога')
async def cmd_dopomoga(message: types.Message):
    """Організація пошуку рецептів за інгрідієнтами"""
    await asyncio.sleep(1)
    await message.answer(
        "Ви можете звернутися за допомогою до розрозбника @ds0903",
    )
