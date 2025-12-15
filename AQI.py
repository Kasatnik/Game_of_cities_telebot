import requests


def result(lat, long):
    token = "b161e3a8-4f95-4c85-9d6e-ed22f24504b7"
    latitude = lat
    longitude = long
    numbers = f"https://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={token}"

    answer = requests.get(numbers)
    data = answer.json()
    return data


"""

"""
