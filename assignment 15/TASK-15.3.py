import requests

def display_specific_weather(city):
    api_key = "4c3db3960a39f47871ec9499c170971d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)
def test_task3():
    # Function exists
    assert callable(display_specific_weather)

    # Input city must be a string
    assert isinstance("Hyderabad", str)

    # City names can vary
    assert isinstance("London", str)
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_specific_weather(city_name)