from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''
Эта клава общая 
?выводится в bot после ответа пользователя на 
команду hello
'''

# фаил menu.py обращается к этим кнопкам
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        
        # первый ряд кнопок
        [
            KeyboardButton(text="Буду"),
            KeyboardButton(text="Неее пицу не хочу"),
        ],
        
        # второй ряд кнопок
        [
            KeyboardButton(text="100")
        ],
        
        # третий ряд кнопок
        [
            KeyboardButton(text="Инлайн меню"),
            KeyboardButton(text="Любой текст"),
            KeyboardButton(text="👍 👍 👍"),
        ]
    ],
    resize_keyboard=True
)
