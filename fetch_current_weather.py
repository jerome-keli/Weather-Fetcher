import requests

def get_weather(api_key, zip_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Creating parameters for the API request
    params = {
        'zip': f'{zip_code},de',  #You can change 'de' to the appropriate country code
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        # Making the API request
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:  #200 means it is okay
            # Print relevant weather information
            print(f"Weather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

#the API key you obtain
api_key = 'YOUR_API_KEY'

# Your desired zip code
zip_code = 'YOUR_DESIRED_ZIP_CODE'

get_weather(api_key, zip_code)

