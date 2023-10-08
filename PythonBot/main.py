#import telebot
#import webbrowser
#import requests # запрос по url адресу
#from telebot import types
#import pymssql
#import pypyodbc as odbc 
#import json # библиотека для работы с документами
# подключение к sql
#from svglib.svglib import svg2rlg #для работы с svg
#from currency_converter import CurrencyConverter
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6590890170:AAEO5qFjyA9BM3BGI4Zh2H5w7BXi_A0AzMQ')

dp = Dispatcher(bot)

# Для sql запросов
""" DRIVER_NAME='SQL SERVER'
SERVER_NAME='DESKTOP-J0NE0CQ\MSSQLSERVER01'
DATABASE_NAME='Test'
conn_str = f'''
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    '''
 """
""" name = '' """
#API для просмотра погоды
""" API = '5619d4ec20e7fdc2a4ec53c616c97865'
currency = CurrencyConverter()
amount = 0 """

#bot = telebot.TeleBot('6590890170:AAEO5qFjyA9BM3BGI4Zh2H5w7BXi_A0AzMQ')# Токен бота который мы хотим поместить

""" 
@bot.message_handler(commands=['start'])#Кнопки передд отправкой сообщения
def start(message):
    markup = types.ReplyKeyboardMarkup() # Функция установки кнопки
    btn1 = types.KeyboardButton('Перейти на сайт ВК')
    markup.row(btn1) # установка кнопки под ответом на фотку
    btn2 = types.KeyboardButton('Удалить фото')
    #murkup.row(btn2)# установка кнопки удаления фотки
    btn3 = types.KeyboardButton('Изменить текст')  
    markup.row(btn2, btn3)# установка кнопки изменения текста
    file = open('./Rushan.jpg', 'rb')
    #bot.send_photo(message.chat.id, file, reply_markup=markup) # Отправка фото от бота
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    #bot.send_audio(message.chat.id, file, reply_markup=markup)# для отправки аудио файла
    #bot.send_video(message.chat.id, file, reply_markup=markup)# для отправки видео файла
    bot.register_next_step_handler(message, on_click)# Функция отслеживающая слеующий шаг, только 1 раз
 """
""" 
def on_click(message):
    if message.text == 'Перейти на сайт ВК':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')
 """
""" 
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://vk.com/im?sel=179653397') # открытие вебсайта

@bot.message_handler(commands=['start']) # команда на которую мы будем отвечать 
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')#переменную message используем для выяснения данных пользователя


@bot.message_handler(commands=['help']) # команда на которую мы будем отвечать 
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html') # parse_mode='html' можно форматировать текст по правилам html 


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}') # reply ответ на предыдущее сообщение
 """
""" 
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup() # Функция установки кнопки

    btn1 = types.InlineKeyboardButton('Перейти на сайт ВК', url='https://vk.com/feed')

    markup.row(btn1) # установка кнопки под ответом на фотку

    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')

    #murkup.row(btn2)# установка кнопки удаления фотки

    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')   


    markup.row(btn2, btn3)# установка кнопки изменения текста

    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)
 """
""" 
@bot.callback_query_handler(func=lambda callback: True) # Перехват callback_data с запросов
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
 """


# Запросы связанные с sql
"""
@bot.message_handler(commands=['start'])
def start(message):
    
    conn = odbc.connect(conn_str)
    #conn = pymssql.connect(server='DESKTOP-J0NE0CQ\MSSQLSERVER01', database='Test')
    cur = conn.cursor()

    cur.execute('''IF OBJECT_ID(N'[dbo].[users]', N'U') IS NULL 
    BEGIN   
	CREATE TABLE [dbo].[users] (
        id int IDENTITY(1,1),
        names varchar(50),
        pass varchar(50),
		PRIMARY KEY(id)
        );
    END;''') # создание таблицы
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip() #strip Удаление пробелов до и после текста
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip() #strip Удаление пробелов до и после текста
    conn = odbc.connect(conn_str)
    cur = conn.cursor()

    com = f"insert into users (names, pass) values('{name}', '{password}')" 

    cur.execute(com) # создание таблицы
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)
    #bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = odbc.connect(conn_str)
    cur = conn.cursor()

    com = "select * from users" 
    cur.execute(com) # создание таблицы
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n' # Вывод данных списка в порядке очереди, второй элемент имя, третий пароль
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)
"""

#Бот погоды можно усовершенствовать
""" 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric') # units=metric для получения градусов цельсия
    if res.status_code == 200: # статус правильной работы, всегда 200
        data = json.loads(res.text) # получение всего текста из страницы(документа)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}') # обращение к документу, через ключи(к температуре)
        image = 'sun.png' if temp < 6.0 else 'sunlight.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else: # если указан несуществующий город
        bot.reply_to(message, 'Город указан не верно!')
 """

#Бот для конвертирования валют
""" 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip()) #конвертация в число
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return


    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')    
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='usd/eur') 
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp') 
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else') 
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше нуля')
        bot.register_next_step_handler(message, summa)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново впистаь сумму')
        bot.register_next_step_handler(call.message, summa) 
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через "/"')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново впистаь сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, f'Что то не так. Впишите значение заново')
        bot.register_next_step_handler(message, my_currency)       
 """

#bot.polling(none_stop=True) # та же самая функция bot.infinity_polling()

# бот на aiogram
""" 
@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    #await message.answer('Hello')
    await message.reply('Hello')

@dp.message_handler(commands=['start'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Site', url='https://vk.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('WebSite'))
    await message.answer('Hello',reply_markup=markup)

"""


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://minify.mobi/results/itproger.com')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


executor.start_polling(dp) # бесконечное действие программы на aiogram
#bot.polling(none_stop=True) # та же самая функция bot.infinity_polling()
