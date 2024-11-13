# third.py
#Quest-bot

import telebot
from AgaspherTKN import tkn
from telebot import types
# Импорт библиотеки telebot, в котором есть функционал для создания ТГ-бота.
bot = telebot.TeleBot(tkn)
# Создается объект BOT из класса TeleBot. Он использует один параметр
# в котором передан API бота.

def main_buttons():
# Создает две кнопки, которые форматируются под размер экрана. 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Покупки🛒')
    itembtn2 = types.KeyboardButton('Задачи💼')
    markup.add(itembtn1, itembtn2)
    return markup

def main_task_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Список задач📋')
    itembtn2 = types.KeyboardButton('Создать задачу📝')
    itembtn3 = types.KeyboardButton('Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup

def generate_list_shop(): # "Покупки"
# Можно сразу выводить список покупок.
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Дополнить список✏')
    itembtn2 = types.KeyboardButton('Убрать позицию💸')
    itembtn3 = types.KeyboardButton('Назад🔙')
    markup.add(itembtn1,itembtn2,itembtn3)
    return markup

def generate_list_task_markup(): # "Список задач".
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Отметить выполненное✅')
    itembtn2 = types.KeyboardButton('Назад🔙')
    markup.add(itembtn1, itembtn2)
    return markup

@bot.message_handler(commands=['start'])
# Команта /start выводит приветственное ообщение бота.
def send_welcome(message):
    markup = main_buttons()
    bot.send_message(message.chat.id, 'Привет! Выбери действие:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
# Ожидания текста от юзера. Этот текст совпадает с тем, что передают созданные ранее кнопки.
# Получается, можно взаимодействовать с ботом без кнопок.
def handle_text(message):
    if message.text == 'Покупки🛒':
        markup = generate_list_shop()
        bot.send_message(message.chat.id, 'Список покупок:', reply_markup=markup)
        #bot.send_message(message.chat.id, 'Меню покупок: /f Пока не готово.')
    elif message.text == 'Задачи💼':
        markup = main_task_buttons()
        bot.send_message(message.chat.id,'Меню задач:',reply_markup=markup)
    elif message.text == 'Список задач📋':
# Здесь будет код для отображения списка задач
        markup = generate_list_task_markup()
        bot.send_message(message.chat.id, 'Список задач:', reply_markup=markup)
    elif message.text == 'Отметить выполненное✅':
# Тут код, отмечающий выполнение задачи.
        bot.send_message(message.chat.id, 'Задача выполнена⭕')
        markup = main_task_buttons() # Переход в главное меню после выполнения задачи.
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
    elif message.text == 'Назад🔙':
# Возврат в главное меню.
        markup = main_buttons() # Переход в главное меню после выполнения задачи.
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
    elif message.text == 'Создать задачу📝':
# Здесь будет код для создания новой задачи
        bot.send_message(message.chat.id, 'Введите новую задачу:')
        bot.register_next_step_handler(message, process_task)

def process_task(message):
# Здесь будет код для сохранения новой задачи
    bot.send_message(message.chat.id, f'Задача "{message.text}" добавлена!')

bot.polling()