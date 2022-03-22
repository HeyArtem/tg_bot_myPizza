from aiogram import types
from loader import dp 


'''
здоровается, выводит id
'''

@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    await message.answer(f"Hi {message.from_user.full_name}\n Is your id: {message.from_user.id}\n(start.py)!")
