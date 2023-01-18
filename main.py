#2 urok
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import config
import sqlite3



backend = KeyboardButton("/backend")
frontend = KeyboardButton("/frontend")
uxui = KeyboardButton("/uxui")
ios = KeyboardButton("/ios")
android = KeyboardButton("/android")

buttons  = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(backend,frontend,uxui,ios,android)

bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect('users.dp')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id_user INTEGER,
    chat_id INTEGER
    );
    """)
connect.commit()

@dp.message_handler(commands = ['start', 'stadying at IT','go'])
async def start(message: types.Message):
    cursor = connect.cursor()
    cursor.execute(f"SELECT id_user FROM users WHERE id_user = {message.from_user.id};")
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}',
        '{message.from_user.first_name}','{message.from_user.last_name}',
        {message.from_user.id}, {message.chat.id})""")
    connect.commit()
    await message.answer(f"Здраствуйте {message.from_user.full_name}",reply_markup=buttons)


@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.reply(f"Вот мои команды: /start, /stadying at IT, /go")


@dp.message_handler(commands="backend")
async def backend(message: types.Message):
    await message.answer(f"Backend - Это внутренняя часть сайта и сервера.",reply_markup=buttons)
    await message.answer(f"Стоимость: 10000сом в месяц")
    await message.answer(f"Обучение: 5 месяц")

@dp.message_handler(commands="frontend")
async def backend(message: types.Message):
    await message.answer(f"Frontend - Это внешняя часть сайта .",reply_markup=buttons)
    await message.answer(f"Стоимость: 11000сом в месяц")
    await message.answer(f"Обучение: 5 месяц")

@dp.message_handler(commands="uxui")
async def backend(message: types.Message):
    await message.answer(f"uxui - Это проектирование удобных, понятных и эстетичных пользовательских интерфейсов .",reply_markup=buttons)
    await message.answer(f"Стоимость: 10000сом в месяц")
    await message.answer(f"Обучение: 5 месяц")

@dp.message_handler(commands="ios")
async def backend(message: types.Message):
    await message.answer(f"ios - Это программа iphone .",reply_markup=buttons)
    await message.answer(f"Стоимость: 15000сом в месяц")
    await message.answer(f"Обучение: 6 месяц")


@dp.message_handler(commands="android")
async def backend(message: types.Message):
    await message.answer(f"ios - Это программа androida .",reply_markup=buttons)
    await message.answer(f"Стоимость: 14000сом в месяц")
    await message.answer(f"Обучение: 8 месяц")


executor.start_polling(dp)
