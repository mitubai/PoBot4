from aiogram import Router, F, types
from aiogram.filters import Command
import logging


start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://mypizza.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://mypizza.kg"),
                types.InlineKeyboardButton(text="Наш твиттер", url="https://mypizza.kg")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Сделать заказ", callback_data="make_order")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "make_order")
async def make_order(callback: types.CallbackQuery):
    await callback.message.answer("Что пожелаете?")