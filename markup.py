
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
# π€ππππβοΈπ πππ­π¬πβοΈβ¬οΈπΊπΏπ§π¬β¬οΈβ‘οΈπ’ππΊπ₯π€

URL = 'https://api.telegram.org/bot'

API_TOKEN = '5571529780:AAFfogvUdAzLitNQfX20VU21WnQm3hBvdZs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = sqlite3.connect('combo.db')



asosiy = ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="π Menyu")

 ],
 [ KeyboardButton(text="π Mening buyurtmalarim")],
  [
 KeyboardButton(text="βοΈ Fikr bildirish"),
 KeyboardButton(text="βοΈ Sozlamalar"),
 ]
 ],
 
 resize_keyboard=True
)


markup_requests = ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="π Geolokatsiani yuboring", request_location=True,request_poll=True)
 ],
  [
 KeyboardButton(text="πΊ Mening manzillarim"),
 KeyboardButton(text="π± Telefon nomerini yuborish" , request_contact=True),
 ],
  [
 KeyboardButton(text="β¬οΈ Ortga",)
 ],
 ],
 
 resize_keyboard=True
)

phone = ReplyKeyboardMarkup(
 keyboard = [
  [

 KeyboardButton(text="π± Telefon nomerini yuborish" , request_contact=True)
 ],
  [
 KeyboardButton(text="β¬οΈ Ortga",)
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
 KeyboardButton(text="π Savat"),
 KeyboardButton(text=" β¬οΈ Ortga"),
 ],
 ],
 
 resize_keyboard=True
)

confirm=ReplyKeyboardMarkup(
 keyboard = [
 [
 KeyboardButton(text="β Yo'q"),
 KeyboardButton(text="β Ha"), 
 ],

 ],
 
 resize_keyboard=True
)

fikr=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='β¬οΈ Ortga')
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
            KeyboardButton(text='β¬οΈ Ortga')
        ]
    ],
    resize_keyboard=True
)

language=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="πΊπΏ O'zbekcha"),
            KeyboardButton(text="π·πΊ Π ΡΡΡΠΊΠΈΠΉ"),

        ],
        [
            KeyboardButton(text='β¬οΈ Ortga')
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
            KeyboardButton(text='β¬οΈ Ortga')
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
    InlineKeyboardButton(text="π₯ Savatga qo'shish", callback_data="Savatga qo'shish")
 ]]
)


backet = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text="π Buyurtma berish", callback_data="Buyurtma"),
        InlineKeyboardButton(text="β° Yetkazib berish vaqti", callback_data="yetkazish"),
    ],
    [   InlineKeyboardButton(text="βοΈ Ortga", callback_data="ortga"),
        InlineKeyboardButton(text="π₯ Savatni tozalash", callback_data="clear")]


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
            KeyboardButton(text="π Savat"),

        ],
        [
            KeyboardButton(text='β¬οΈ Ortga')
        ]
    ],
    resize_keyboard=True
)

@dp.callback_query_handler(text=['Buyurtma'])
async def sendphone(message: Message):
    await bot.send_message(message.from_user.id, """Telefon raqamingizni quyidagi formatda yuboring yoki kiriting: +998 ** *** ** **
Eslatma: Agar siz onlayn buyurtma uchun Click yoki Payme orqali toΚ»lashni rejalashtirmoqchi boΚ»lsangiz, tegishli xizmatda hisob qaydnomasi roΚ»yxatdan oΚ»tgan telefon raqamini koΚ»rsating.""", reply_markup=phone)


# @dp.callback_query_handler(text=["Buyurtma"])
# async def buyurtma1(call:CallbackQuery):
#     await call.message ("Yuborilgan nomer qilindi qulab ")

@dp.message_handler(text=["π Savat"])
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



@dp.message_handler(text=["πΊπΏ O'zbekcha"])
async def send_settings(message: Message):
    await bot.send_message(message.from_user.id, "Tayyor", reply_markup=asosiy)

@dp.message_handler(text=["βοΈ Sozlamalar"])
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

@dp.message_handler(text=["π Geolokatsiani yuboring"])
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

@dp.message_handler(text=["β Ha"])
async def send_section1(message: Message):
    await bot.send_message(message.from_user.id, "Bo'limni tanlang", reply_markup=section)

@dp.message_handler(text=["β Yo'q"])
async def send_section2(message: Message):
    await bot.send_message(message.from_user.id, "π Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=markup_requests)

@dp.message_handler(text=["βοΈ Fikr bildirish"])
async def send_idea(message: types.Message):
    print(send_idea)
    await bot.send_message(message.from_user.id, "Fikringizni yuboring", reply_markup=fikr)


@dp.message_handler(text=["β¬οΈ Ortga"])
async def send_asosiy(message: Message):
    await bot.send_message(message.from_user.id, "Bizning Tugmalar", reply_markup=asosiy)

@dp.message_handler(commands=["start"])
async def send_basic(message: Message):
    await bot.send_message(message.from_user.id, "Bizning Tugmalar", reply_markup=asosiy)

@dp.message_handler(text=["π Menyu"])
async def send_menu(message: Message):
    await bot.send_message(message.from_user.id, "π Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=markup_requests)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)