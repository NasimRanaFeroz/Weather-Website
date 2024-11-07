import requests
from dotenv import load_dotenv
import os
from pprint import pprint 

load_dotenv()

def get_current_weather(city="Dhaka"):
    req_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    if not bool(city.strip()):
        city = "Dhaka"

    weather_data = requests.get(req_url).json()
    return weather_data

if __name__ == '__main__':
    current_weather = get_current_weather()
    pprint(current_weather) 
