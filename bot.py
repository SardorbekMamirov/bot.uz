# from cgitb import text
# import logging
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.types import Message, ReplyKeyboardRemove
# from aiogram import types


# URL = 'https://api.telegram.org/bot'

# API_TOKEN = '5312087196:AAHr59H_i8GctEDas7ovjd1s7fDbxcWVPms'

# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# asosiy = ReplyKeyboardMarkup(
#  keyboard = [
#  [
#  KeyboardButton(text="Menyu")

#  ],
#  [ KeyboardButton(text="Mening buyurtmalarim")],

#   [
#  KeyboardButton(text="Fikr bildirish"),
#  KeyboardButton(text="Sozlamalar"),
#  ]
#  ],
 
#  resize_keyboard=True
# )

# menyu = ReplyKeyboardMarkup(
#  keyboard = [
#  [
#  KeyboardButton(text="Menyu")

#  ],
#  [ KeyboardButton(text="Mening buyurtmalarim")],

#   [
#  KeyboardButton(text="Fikr bildirish"),
#  KeyboardButton(text="Sozlamalar"),
#  ]
#  ],
 
#  resize_keyboard=True
# )

# @dp.message_handler(text=["hi"])
# async def send_language(message: Message):
#     await bot.send_message(message.from_user.id, "Bizning Tugmalar", reply_markup=markup_requests)


# markup_requests = ReplyKeyboardMarkup(resize_keyboard=True)\
#     .add(KeyboardButton("Kontaktingizni jo'nating", request_contact=True)).add(KeyboardButton('Geolokatsiangizni jo\'nating', request_location=True))

# @dp.message_handler(Command('start'))
# async def show_asosiy(message: types.Message):
#  await message.reply("""Assalomu alaykum !!!\n Support Solution Restoranbotiga Xush kelibsiz !!!\n 
# #     Здравствуйте !!!\n Добро пожаловать в Support Solution  Restaurant\n
# #     Hello !!!\n Welcome to Support Solution Restaurant""", reply_markup=asosiy)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)