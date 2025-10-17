import requests

def get_weather(city):
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Temperature in {city}: {temp}°C")
        print(f"Weather description: {desc}")
    else:
        print("City not found or API error.")

city = input("Enter city name: ")
get_weather(city)
