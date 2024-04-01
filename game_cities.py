import random
import json
import telebot as tel
import os
import pyautogui
import geonamescache

from AQI import result

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

token = "6630004707:AAGbviWPwvbAl7oaAKD9WCOV-SdCG4oWjNE"
bot = tel.TeleBot(token)
creator = 6735254429
dict_id = {}
written_user_cities = []


@bot.message_handler(commands=["start_game"])
def start(message):
    bot.send_message(message.from_user.id,
                     "Привет, это игра в города напиши название города. Но писать название надо с большой буквы!")


@bot.message_handler(content_types=["text"])
def user_message(message):
    user_city = message.text
    l = gc.search_cities(user_city, case_sensitive=True, contains_search=True)
    if len(written_user_cities) > 0:
        latest_bot_letter = (written_user_cities[-1][-1])
        if latest_bot_letter in ["ь", "ъ", "ы"]:
            latest_bot_letter = written_user_cities[-1][-2].upper()
        if latest_bot_letter != user_city[0]:
            bot.send_message(message.from_user.id, "Ты написал не на ту букву")
            return





    if not l:
        bot.send_message(message.from_user.id, "Такого города нет")
        return
    if user_city in written_user_cities:
        bot.send_message(message.from_user.id, "Этот город уже был")
        return


    written_user_cities.append(user_city)
    latest_letter = user_city[-1]
    if latest_letter in ["ь", "ъ", "ы"]:
        latest_letter = user_city[-2]
    written_bot_cities = searching_cities(latest_letter)
    written_user_cities.append(written_bot_cities)

    bot.send_message(message.from_user.id, f"Я говорю на букву: {latest_letter}")
    bot.send_message(message.from_user.id, written_bot_cities)
    print(written_user_cities)
def searching_cities(latest_letter):
    latest_letter = latest_letter.upper()
    for v in cities:
        names = cities[v]["alternatenames"]
        for h in names:
            if h:
                if h in written_user_cities:
                    break
                if h[0] == latest_letter:
                        return h


@bot.message_handler(content_types=["location"])
def user_location(message):
    result(message.location.latitude, message.location.longitude)


def open_file_r(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def open_file_w(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


bot.polling()


"""
В этом коде создать таблицу БД для юзеров с такими столбцами: айди_тг, юзернейм, имя_фамилия, поинты
Когда человек нажимает на команду "старт", просто записать пользователя в БД (инсерт)
"""