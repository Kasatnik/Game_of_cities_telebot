import random
import json
import telebot as tel
import os
import pyautogui
import cv2
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = ""
bot = tel.TeleBot(token)
creator =
dict_id = {}


@bot.message_handler(commands=["start"])
def start(message):
    pass


def open_file_r(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def open_file_w(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


bot.polling()
