import asyncio
from aiogram import F
# from datetime import datetime
from aiogram import Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from handlers.logic import search_films

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):

    text = (
        "Привіт, я був створений для того аби допомогти вам знайти потрібний фільм."
        )
    text1 = (
        "будьласка оберіть потрбіну вам дію"
        )

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

    text1 = str("Напишіть будьласка жанр фільму який ви бажаєте знайти")
    text2 = str("\nНаприклад 'драма'")
    text3 = str("Також ви можете повернутися в меню або натиснувши кнопку новинки моментально ортимати список свіжих фільмів")
    full_text = text1+text2
    await message.reply(full_text, reply_markup=types.ReplyKeyboardRemove())

    await asyncio.sleep(2)
    await message.answer(text3, reply_markup=keyboard)

    @router.message()
    async def cmd_novinki(message: types.Message):
        films = message.text
        name, zhanr, year, rating = await search_films(films)

        if name:
            await message.answer("👾")
            await message.answer(f"Знайдено фільм на вечір 👾: \nім'я: {name}\nжанр: {zhanr}\nрік: {year}\nрейтинг: {rating}")
        else:
            await message.answer("Фільм не знайдено")

@router.message(lambda message: message.text == 'Меню')
async def show_menu(message: types.Message):

    await cmd_start(message)

@router.message(lambda message: message.text == 'Новинки')
async def cmd_novinki(message: types.Message):

    await message.reply("Для повернення в меню пиши Меню")




@router.message(lambda message: message.text == 'Допомога')
async def cmd_dopomoga(message: types.Message):
    text = str(
        "Ви можете звернутися за допомогою до розрозбника @ds0903",
    )
    await message.reply(text, reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [KeyboardButton(text="Меню")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(2)
    await message.answer("абож ви можете повернутися в меню", reply_markup=keyboard)


    # @router.message()
    # async def cmd_novinki(message: types.Message):
    #     films = message.text
    #     film = await search_films(films)
    #     if film:
    #         await message.answer(f"фільм знайдено:  {film}")
    #     else:
    #         text = str("Такого фільму немає")