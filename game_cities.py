import random
import json
import telebot as tel
import os
import pyautogui
import cv2
import geonamescache

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

token = "6630004707:AAGbviWPwvbAl7oaAKD9WCOV-SdCG4oWjNE"
bot = tel.TeleBot(token)
creator = 6735254429
dict_id = {}


@bot.message_handler(commands=["start_game"])
def start(message):
    bot.send_message(message.from_user.id, "Напиши название города")


@bot.message_handler(content_types=["text"])
def user_message(message):
    user_city = message.text
    print(gc.search_cities(user_city, case_sensitive=True, contains_search=True))


def open_file_r(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def open_file_w(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


bot.polling()
