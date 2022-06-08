
from cgitb import text
from email import message
import logging
from operator import countOf
from urllib import response
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,CallbackQuery
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram .types import ReplyKeyboardMarkup, KeyboardButton,Message, Location
import sqlite3

from django.urls import is_valid_path
# 🤚👌👍👉👇⚙️🛠🛍🛒📭📬🗑✏️⬅️🇺🇿🇧🇬⬇️➡️💢📍🗺📥📤

URL = 'https://api.telegram.org/bot'

API_TOKEN = '5571529780:AAFfogvUdAzLitNQfX20VU21WnQm3hBvdZs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = sqlite3.connect('combo.db')



asosiy = ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="📃 Menyu")

 ],
 [ KeyboardButton(text="🛍 Mening buyurtmalarim")],
  [
 KeyboardButton(text="✏️ Fikr bildirish"),
 KeyboardButton(text="⚙️ Sozlamalar"),
 ]
 ],
 
 resize_keyboard=True
)


markup_requests = ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="📍 Geolokatsiani yuboring", request_location=True,request_poll=True)
 ],
  [
 KeyboardButton(text="🗺 Mening manzillarim"),
 KeyboardButton(text="📱 Telefon nomerini yuborish" , request_contact=True),
 ],
  [
 KeyboardButton(text="⬅️ Ortga",)
 ],
 ],
 
 resize_keyboard=True
)

phone = ReplyKeyboardMarkup(
 keyboard = [
  [

 KeyboardButton(text="📱 Telefon nomerini yuborish" , request_contact=True)
 ],
  [
 KeyboardButton(text="⬅️ Ortga",)
 ],
 ],
 
 resize_keyboard=True
)



section = ReplyKeyboardMarkup(
 keyboard = [

  [
 KeyboardButton(text="Set"),
 KeyboardButton(text="Lavash"),
 ],
[
 KeyboardButton(text="Shaurma"),
 KeyboardButton(text="Donar"),
 ],
 [
 KeyboardButton(text="Burger"),
 KeyboardButton(text="Hot dog"),
 ],
 [
 KeyboardButton(text="Shirinliklar yoki disertlar"),
 KeyboardButton(text="Ichimliklar"),
 ],
 [
 KeyboardButton(text="Garnir"),
 ],
  [
 KeyboardButton(text="🛒 Savat"),
 KeyboardButton(text=" ⬅️ Ortga"),
 ],
 ],
 
 resize_keyboard=True
)

confirm=ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="❌ Yo'q"),
 KeyboardButton(text="✅ Ha"), 
 ],

 ],
 
 resize_keyboard=True
)

fikr=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)

settings_language=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)

language=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский"),

        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)

set=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="COMBO+"),
            KeyboardButton(text="Kids COMBO"),

        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)
count1=1
if count1:
    count1!=1
    count1+1

cb=CallbackData('buy', 'id', 'name', 'price')
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard = [[
    InlineKeyboardButton(text="-", callback_data="Minus"),
    InlineKeyboardButton(text=count1, callback_data="Count"),
    InlineKeyboardButton(text="+", callback_data="Plus")
    ],
    [
    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="Savatga qo'shish")
 ]]
)


backet = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text="🚙 Buyurtma berish", callback_data="Buyurtma"),
        InlineKeyboardButton(text="⏰ Yetkazib berish vaqti", callback_data="yetkazish"),
    ],
    [   InlineKeyboardButton(text="◀️ Ortga", callback_data="ortga"),
        InlineKeyboardButton(text="📥 Savatni tozalash", callback_data="clear")]


    ]
)

# phone_key = InlineKeyboardMarkup(
#     inline_keyboard = [[
#     InlineKeyboardButton(text="Sotib olish", callback_data="Sotib olish")
#  ]]
# )

# mac_key = InlineKeyboardMarkup(
#     inline_keyboard = [[
#     InlineKeyboardButton(text="Sotib olish mac", callback_data="Sotib olish mac")
#  ]]
# )

combo2=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Savat"),

        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)

@dp.callback_query_handler(text=['Buyurtma'])
async def sendphone(message: Message):
    await bot.send_message(message.from_user.id, """Telefon raqamingizni quyidagi formatda yuboring yoki kiriting: +998 ** *** ** **
Eslatma: Agar siz onlayn buyurtma uchun Click yoki Payme orqali toʻlashni rejalashtirmoqchi boʻlsangiz, tegishli xizmatda hisob qaydnomasi roʻyxatdan oʻtgan telefon raqamini koʻrsating.""", reply_markup=phone)


# @dp.callback_query_handler(text=["Buyurtma"])
# async def buyurtma1(call:CallbackQuery):
#     await call.message ("Yuborilgan nomer qilindi qulab ")

@dp.message_handler(text=["🛒 Savat"])
async def send_settings(message: Message):
    await bot.send_message(message.from_user.id, "Vaqtichalik savatda hech narsa yo'q", reply_markup=backet)


@dp.message_handler(text=["COMBO+"])
async def send_settings(message: Message):
    photo = open('files/photo2_2022-05-23_09-06-24.jpg', 'rb')
    await bot.send_message(message.from_user.id, "Quyidagilardan birini tanlang", reply_markup=combo2)
    await message.answer_photo(photo, """Eng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi
 Narxi: 14 000 so'm""", reply_markup=keyboard1)
    

# @dp.callback_query_handler(text_contains='Phone')
# async def phone(call:CallbackQuery):

#     await call.message.answer('Sotib olish', reply_markup=phone_key)

# @dp.callback_query_handler(text_contains='iphone 13')
# async def mac(call:CallbackQuery):
#     await call.answer(cache_time=50)

#     await call.message.answer('Sotib olish', reply_markup=mac_key)
@dp.callback_query_handler(text=["Minus"])
async def minus(call:CallbackQuery):
    await ("Savatga qo'shilishi kk")

@dp.callback_query_handler(text=["Plus"])
async def plus(call:CallbackQuery):
    await call.answer(count1)

@dp.callback_query_handler(text=["Count"])
async def count(call:CallbackQuery):
    await call.answer("Savatga qo'shilishi kk")

@dp.callback_query_handler(text=["Savatga qo'shish"])
async def mac(call:CallbackQuery):
    await call.answer("Savatga qo'shilmoqda", show_alert=True)


@dp.message_handler(commands=["help"])
async def send_help(message: Message):
    await bot.send_message(message.from_user.id, "Assalomu Alaykum siz HELP tugmasini bosdingiz sizga qanday yordam bera olamiz!!!")

# @dp.message_handler(text=["COMBO+"])
# async def send_combo(message: Message):
#     photo = open('files/photo2_2022-05-23_09-06-24.jpg', 'rb')
#     await bot.send_photo(message.from_user.id, photo, """Eng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi
#  Narxi: 14 000 so'm""", reply_markup=combo)

@dp.message_handler(content_types=['contact'])
async def send_phone(message: Message):
    print(message.contact)
    await bot.send_message(message.from_user.id, "Yuborilgan nomer qabul qilindi")

@dp.message_handler(text=["Set"])
async def send_set(message: Message):
    photo = open('files/set_photo_2022-06-01_12-25-07.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=set)


@dp.message_handler(text=["Tilni o'zgartirish"])
async def send_settings(message: Message):
    await bot.send_message(message.from_user.id, "Tilni tanlang", reply_markup=language)



@dp.message_handler(text=["🇺🇿 O'zbekcha"])
async def send_settings(message: Message):
    await bot.send_message(message.from_user.id, "Tayyor", reply_markup=asosiy)

@dp.message_handler(text=["⚙️ Sozlamalar"])
async def send_settings(message: Message):
    await bot.send_message(message.from_user.id, "Harakatni tanlang", reply_markup=settings_language)


@dp.message_handler(content_types=['location'])
async def send_location(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "Buyurtma bermoqchi bo'lgan manzil latitude:  {}\nlongitude: {} : Ushbu manzilni tasdiqlaysizmi".format(lat, lon)
    print(reply)
    await message.answer(reply, reply_markup=confirm)
    # geolocator = Nominatim(user_agent="geoapiExercises") 
    # location = geolocator.geocode(str(message.location.latitude)+","+str(message.location.longitude))

@dp.message_handler(text=["📍 Geolokatsiani yuboring"])
async def send_location(message: Message):
    # geolocator = Nominatim(user_agent="geoapiExercises") 
    # location = geolocator.geocode(str(message.location.latitude)+","+str(message.location.longitude))
    await bot.send_message(message.from_user.id, "Sizning joylashuvingiz haqida ma'lumot to'g'rimi", reply_markup=confirm)

# @dp.message_handler(content_types=['location'])
# async def handle_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
#     await message.answer(reply, reply_markup=types.ReplyKeyboardRemove(confirm))

@dp.message_handler(text=["✅ Ha"])
async def send_section1(message: Message):
    await bot.send_message(message.from_user.id, "Bo'limni tanlang", reply_markup=section)

@dp.message_handler(text=["❌ Yo'q"])
async def send_section2(message: Message):
    await bot.send_message(message.from_user.id, "📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=markup_requests)

@dp.message_handler(text=["✏️ Fikr bildirish"])
async def send_idea(message: types.Message):
    print(send_idea)
    await bot.send_message(message.from_user.id, "Fikringizni yuboring", reply_markup=fikr)


@dp.message_handler(text=["⬅️ Ortga"])
async def send_asosiy(message: Message):
    await bot.send_message(message.from_user.id, "Bizning Tugmalar", reply_markup=asosiy)

@dp.message_handler(commands=["start"])
async def send_basic(message: Message):
    await bot.send_message(message.from_user.id, "Bizning Tugmalar", reply_markup=asosiy)

@dp.message_handler(text=["📃 Menyu"])
async def send_menu(message: Message):
    await bot.send_message(message.from_user.id, "📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=markup_requests)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)