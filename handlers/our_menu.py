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


# lambda m: m.text.lower() == "пицца"
@menu_router.message(F.text.lower() == "пицца 30 см")
async def show_pizzas(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    # DB request
    await message.answer("Вот пиццы, которые мы предлагаем", reply_markup=kb)


@menu_router.message(F.text.lower() == "закуски")
async def show_snacks(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    # DB request
    # all_dishes = db.get_all_dishes()
    await message.answer("Вот закуски, которые мы предлагаем", reply_markup=kb)