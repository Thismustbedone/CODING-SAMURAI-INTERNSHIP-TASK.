import requests

def get_weather(city, api_key):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "current" in data:
            weather = {
                "city": data["location"]["name"],
                "temperature": data["current"]["temperature"],
                "description": data["current"]["weather_descriptions"][0],
            }
            return weather
        else:
            print(f"API error: {data.get('error', {}).get('info', 'Unknown error')}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def main():
    api_key = "c7ef01d2a1e46fed3ad692fe19e3a2af" 
    city = input("Enter city name: ")
    weather = get_weather(city, api_key)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    main()