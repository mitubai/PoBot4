import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(file, caption="Котик")
    await message.reply("Котик")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет")
    await message.answer(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())