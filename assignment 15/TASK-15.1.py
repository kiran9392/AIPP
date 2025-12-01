import requests
import json

def get_weather(city):
    api_key = "4c3db3960a39f47871ec9499c170971d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.json())
        return

    data = response.json()
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
