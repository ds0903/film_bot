import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from handlers import comands

# Головний файл бота
# ## НЕ ЧІПАЙ бо буде торба !!! ###
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

dp.include_router(comands.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# ## НЕ ЧІПАЙ бо буде торба !!! ###
