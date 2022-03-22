from aiogram import types


'''
это вывод описания команд (контекст) прописанных в users, 
описания выводятся даже если для них нет скрипта в users
'''

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
    types.BotCommand("start", "запустить бота"),
    types.BotCommand("help", "Нужна помощь?"),    
    types.BotCommand("menu", "Братишка выбери ответ"),
    types.BotCommand("hello", "Вечер в хату Я Василий. Есть только пицца. Будешь?")
])
