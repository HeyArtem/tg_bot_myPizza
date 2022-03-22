from aiogram import types
from loader import dp 

'''
выводит
Вечер в хату Art.

"Я Василий. Есть только пицца. Будешь?"
'''
@dp.message_handler(text="/hello")
async def command_hello(message: types.Message):
    await message.answer(f"Вечер в хату {message.from_user.full_name}.\nЯ Василий. Есть только пицца. Будешь?")
