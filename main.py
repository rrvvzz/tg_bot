import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city,open_weather_token):

    code_to_smile = {
        "Clear" : "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        country = data["sys"]["country"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно"

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nСтрана: {country} \nТемпература: {temp} С  {wd}\nВлажность: {humidity} %\n"
              f"Скорость ветра: {wind} м/с\nВосход солнца: {sunrise} \nЗакат: {sunset} \n")


    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город:  ")
    get_weather(city,open_weather_token)


if __name__ == '__main__':
    main()