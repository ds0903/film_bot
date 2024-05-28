import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from handlers.logic import (search_films_new, search_films_year,
                            search_films_zhanr)

router = Router()


class Form(StatesGroup):
    waiting_for_zhanr = State()
    waiting_for_year = State()


@router.message(Command("start"))
async def cmd_start(message: types.Message):

    text = "Привіт, я був створений для того аби допомогти вам знайти потрібний фільм."
    text1 = "будьласка оберіть потрібну вам дію"

    kb = [
        [KeyboardButton(text="Почати пошук"), KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text)
    await asyncio.sleep(1)
    await message.answer(text1, reply_markup=keyboard)


@router.message(lambda message: message.text == "Почати пошук")
async def cmd_poshuk_films(message: types.Message):
    """Організація пошуку фільма за критеріями"""
    kb = [
        [KeyboardButton(text="Пошук по рокам"), KeyboardButton(text="Пошук по жанру")],
        [KeyboardButton(text="Допомога")],
        [KeyboardButton(text="Новинки"), KeyboardButton(text="Меню")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    text3 = str("Оберіть потрібну вам дію")
    await asyncio.sleep(1)
    await message.answer(text3, reply_markup=keyboard)


@router.message(lambda message: message.text == "Меню")
async def show_menu(message: types.Message):

    await cmd_start(message)


@router.message(lambda message: message.text == "Новинки")
async def cmd_novinki(message: types.Message):
    text = "Планета обезьян"
    name, zhanr, year, rating = await search_films_new(text)
    text1 = f"Свіжий фільм на вечір: \nім'я: {name}\nжанр: {zhanr}\nрік{year}\nрейтинг: {rating}"
    await message.reply(text1, reply_markup=types.ReplyKeyboardRemove())
    await return_menu(message)


@router.message(lambda message: message.text == "Назад")
async def return_menu(message: types.Message):
    """Повертаємось на пункт назад після пошуку"""
    kb = [
        [KeyboardButton(text="Почати пошук"), KeyboardButton(text="Меню")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(2)
    await message.reply(
        "Для повернення в меню тисни кнопку або спробуй ще щось знайти",
        reply_markup=keyboard,
    )


@router.message(lambda message: message.text == "Пошук по жанру")
async def cmd_zhanr(message: types.Message, state: FSMContext):

    await message.reply(
        "Напишіть жанр фільму", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(Form.waiting_for_zhanr)

    @router.message(Form.waiting_for_zhanr)
    async def cmd_zhanr(message: types.Message):
        films = message.text
        name, zhanr, year, rating = await search_films_zhanr(films)

        if zhanr:
            await message.answer("👾")
            await message.answer(
                f"Знайдено фільм на вечір: \nім'я: {name}\nжанр: {zhanr}\nрік: {year}\nрейтинг: {rating}"
            )
            await return_menu(message)
            await state.clear()
        else:
            await message.answer("Фільм не знайдено")
            await return_menu(message)


@router.message(lambda message: message.text == "Пошук по рокам")
async def cmd_roki(message: types.Message, state: FSMContext):

    await message.reply(
        "Напишіть рік випуску фільму", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(Form.waiting_for_year)

    @router.message(Form.waiting_for_year)
    async def cmd_year(message: types.Message):
        films = message.text
        name, zhanr, year, rating = await search_films_year(films)

        if year:
            await message.answer("👾")
            await message.answer(
                f"Знайдено фільм на вечір: \nім'я: {name}\nжанр: {zhanr}\nрік: {year}\nрейтинг: {rating}"
            )
            await return_menu(message)
            await state.clear()
        else:
            await message.answer("Фільм не знайдено")
            await return_menu(message)


@router.message(lambda message: message.text == "Допомога")
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

    #     @router.message()
    # async def cmd_novinki(message: types.Message):
    #     films = message.text
    #     name, zhanr, year, rating = await search_films(films)

    #     if name:
    #         await message.answer("👾")
    #         await message.answer(f"Знайдено фільм на вечір 👾: \nім'я: {name}\nжанр: {zhanr}\nрік: {year}\nрейтинг: {rating}")
    #     else:
    #         await message.answer("Фільм не знайдено")
    # await message.reply(full_text, reply_markup=types.ReplyKeyboardRemove())
