from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers import dp
from aiogram import executor

'''
Главный файл, его всегда запускаю
'''

async def on_startup(dp):
    
    await on_startup_notify(dp)
    await set_default_commands(dp)
    
    # выводится в терминале
    print("Bot is Running!!!")
    

# здесь запуск без main. Попробовать исправить!!
# def main():

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)

    