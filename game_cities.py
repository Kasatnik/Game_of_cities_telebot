import random
import json
import time
import telebot as tel
import geonamescache
from AQI import result
import wikipedia
import requests

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

token = "6530281381:AAE4bOrzoIYULEHWiF8tdf6R20oYez8v1OQ"
images_api = "bAKzpGjWfG25uqAIVVt-NqfFbokGXxP3-DxQaVcAINk"
bot = tel.TeleBot(token)
creator = 6735254429
dict_id = {}
written_user_cities = []


@bot.message_handler(commands=["start_game"])
def start(message):
    bot.send_message(message.from_user.id,
                     "Привет, это игра в города напиши название города. Но писать название надо с большой буквы!")


@bot.message_handler(commands=["reset_words"])
def reset(message):
    written_user_cities.clear()
    bot.send_message(message.from_user.id, "Города были сброшены")


@bot.message_handler(content_types=["text"])
def user_message(message):
    user_city = message.text
    l = gc.search_cities(user_city, case_sensitive=True, contains_search=True)
    if len(written_user_cities) > 0:
        latest_bot_letter = (written_user_cities[-1][-1].upper())
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
    user_lat = l[0]["latitude"]
    user_long = l[0]["longitude"]
    bot.send_location(message.from_user.id, user_lat, user_long)
    answer = wiki(message, user_city)
    send_data(message, user_lat, user_long, answer)

    time.sleep(0)

    written_user_cities.append(user_city)
    latest_letter = user_city[-1]
    print(written_user_cities)
    if latest_letter in ["ь", "ъ", "ы"]:
        latest_letter = user_city[-2]
    written_bot_cities, lat, long = searching_cities(latest_letter)
    written_user_cities.append(written_bot_cities)

    bot.send_message(message.from_user.id, f"Я говорю на букву: {latest_letter}\n\n{written_bot_cities}")
    bot.send_location(message.from_user.id, lat, long)
    answerr = wiki(message, written_bot_cities)
    send_data(message, lat, long, answerr)

def searching_cities(latest_letter):
    latest_letter = latest_letter.upper()
    for v in cities:
        names = cities[v]["alternatenames"]
        for h in names:
            if h:
                if h in written_user_cities:
                    break
                if h[0] == latest_letter:
                    return h, cities[v]["latitude"], cities[v]["longitude"]


@bot.message_handler(content_types=["location"])
def user_location(message):
    send_data(message, message.location.latitude, message.location.longitude)


def send_data(message, lat, long, answer):
    data = result(lat, long)
    print(11111111, data)
    if data["status"] == 'fail':
        print("Status")
        return
    launch_url_img = url_img(user_city=data["data"]["state"])
    country = data["data"]["country"]
    tp = data["data"]["current"]["weather"]["tp"]
    aqius = data["data"]["current"]["pollution"]["aqius"]
    ws = data["data"]["current"]["weather"]["ws"]
    if launch_url_img is not None:
        bot.send_photo(message.from_user.id, launch_url_img)
        bot.send_message(message.from_user.id,
                         f"Страна: {country},\nТемпература: {tp},\nЗагрязнённость воздуха: {aqius},\nCкорость ветра: {ws}\n\n{answer}")
    else:
        bot.send_message(message.from_user.id,
                         f"Страна: {country},\nТемпература: {tp},\nЗагрязнённость воздуха: {aqius},\nCкорость ветра: {ws}\n\n{answer}")


def wiki(message, user_city):
    wikipedia.set_lang('ru')
    try:
        python_page = wikipedia.page(user_city)
        return python_page.summary

    except wikipedia.exceptions.PageError:
        return "  "
    except wikipedia.exceptions.DisambiguationError:
        return "  "


def url_img(user_city):
    url = f"https://api.unsplash.com/search/photos?page=1&query={user_city}&client_id={images_api}"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        results = json_data["results"]
        if results:
            random_img = random.choice(results)
            return random_img["urls"]["regular"]
    return None


def open_file_r(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data



def open_file_w(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


bot.polling()
