from aiogram .types import ReplyKeyboardMarkup, KeyboardButton

btnhello = KeyboardButton("Assalomu Alaykum")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnhello)

button1 =KeyboardButton("Menyu")
button2 =KeyboardButton("Mening Buyurtmalarim")
button3 =KeyboardButton("Fikr bildirish")
button3 =KeyboardButton("Settings")


markup_requests = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton("Kontaktingizni jo'nating", request_contact=True)).add(KeyboardButton('Geolokatsiangizni jo\'nating', request_location=True))
