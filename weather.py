import requests

API_KEY = "your_api_key"  # Replace with your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)

    if weather:
        print(f"\n🌍 Weather in {weather['city']}")
        print(f"🌡️ Temperature: {weather['temperature']}°C")
        print(f"☁️ Condition: {weather['description']}")
        print(f"💦 Humidity: {weather['humidity']}%")
        print(f"💨 Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("❌ City not found. Please try again.")

if __name__ == "__main__":
    main()
