import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather(city="Dhaka"):
    if not bool(city.strip()):
        city = "Dhaka"
    
    # Construct the request URL
    api_key = os.getenv("API_KEY")
    req_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'
    
    response = requests.get(req_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None 

if __name__ == '__main__':
    # For local testing purposes
    from pprint import pprint
    current_weather = get_current_weather()
    pprint(current_weather)
