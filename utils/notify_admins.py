import logging
from aiogram import Dispatcher
from data.config import admins_id


'''
Скрипт проходит в цикле по id админов
(берет их из config.py)
отправляет в tg bot сообщение о запуске бота

'''
async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        
        try:
            text = 'Bot is running !!! ("on_startUp_notify.py")'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            print("Ушел в except (notify_admins.py)")
