from bot import db
from aiogram import Router, F, types


menu_router = Router()

@menu_router.callback_query(F.data == "our_menu")
async def make_order(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Пицца 30 см"),
                types.KeyboardButton(text="Пицца 40 см")
            ],
            [
                types.KeyboardButton(text="Закуски"),
            ],
            [
                types.KeyboardButton(text="Салаты")
            ],
            [
                types.KeyboardButton(text="Супы"),
            ]
        ]
    )
    await callback.message.answer("Что пожелаете?", reply_markup=kb)
# @menu_router.message(F.text.lower() == "пицца 30 см")
# async def show_pizzas(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     # DB request
#     dishes = db.get_dishes_by_cat_name("пицца 30")
#     await message.answer("Вот пиццы, которые мы предлагаем", reply_markup=kb)
#     for dish in dishes:
#         await message.answer(f"Название{dish[1]}\n, Описание: {dish[2]}\n, Цена: {dish[3]}")

# @menu_router.message(F.text.lower() == "пицца 40 см")
# async def show_pizzas(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     # DB request
#     dishes = db.get_dishes_by_cat_name("пицца 40")
#     await message.answer("Вот пиццы, которые мы предлагаем", reply_markup=kb)
#     for dish in dishes:
#         await message.answer(f"Название{dish[1]}\n, Описание: {dish[2]}\n, Цена: {dish[3]}")

# @menu_router.message(F.text.lower() == "закуски")
# async def show_snacks(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     # DB request
#     dishes = db.get_dishes_by_cat_name("Закуски")
#     await message.answer("Вот закуски, которые мы предлагаем", reply_markup=kb)
#     for dish in dishes:
#         await message.answer(f"Название{dish[1]}\n, Описание: {dish[2]}\n, Цена: {dish[3]}")


dishes_categories = ("закуски", "салаты", "супы", "пицца 30 см", "пицца 40 см")
@menu_router.message(F.text.lower().in_(dishes_categories))
async def show_dishes_of_category(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    # DB request
    category = db.get_category_by_name(message.text)
    dishes = db.get_dishes_by_cat_name(message.text)
    await message.answer(category[2], reply_markup=kb)
    for dish in dishes:
        await message.answer(f"Название{dish[1]}\nОписание: {dish[2]}\nЦена: {dish[3]}")
