from loader import dp 
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import main_keyboard


'''
Выводит надпись "Братишка выбери ответ"
и клавиатуру main_keyboard!!
'''


# отвечает на сообщение и вызывает клаву Да или Нет
@dp.message_handler(Command("menu"))
async def command_menu(message: types.Message):
    
    # 1-й параметр (сообщение в боте), второй(вызываю клавиатуру из keyboards/default/keyboard_menu.py)
    await message.answer("Братишка выбери ответ", reply_markup=main_keyboard)
