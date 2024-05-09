import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    print("URL:", url)  # Print the URL for debugging purposes
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

def main():
    api_key = "9c43f19bab2f4789be743457775b5cb4"  # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
    location = input("Enter city name or city name, country code (e.g., Hyderabad, IN): ")

    weather_info = get_weather(api_key, location)

    if weather_info:
        print(f"Weather in {location}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Description: {weather_info['description']}")
    else:
        print("Could not fetch weather data. Please check your input.")

if __name__ == "__main__":
    main()
