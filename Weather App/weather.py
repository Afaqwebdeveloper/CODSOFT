import requests

def get_weather_data(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric", 
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather(data):
    if data:
        main_info = data['main']
        weather_info = data['weather'][0]

        temperature = main_info['temp']
        humidity = main_info['humidity']
        description = weather_info['description']

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")

def main():
    api_key = "7fe109373074da50c770401378f11252"  
    location = input("Enter the name of a city or city, country: ")

    data = get_weather_data(location, api_key)

    if data:
        display_weather(data)
    else:
        print("Weather data not available for the specified location.")

if __name__ == "__main__":
    main()
