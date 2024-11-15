# City Weather Checker

This is a Flask web application that allows users to check the current weather for any city using data from the OpenWeather API. It provides information such as temperature, weather description, and the "feels like" temperature.

## Features

- Display current weather data (temperature, weather description, feels like temperature) for a city.
- Default city is set to "Dhaka" if no city is provided.
- Option to input any city name via URL query parameters.

## How to Use

1. **Access the website:**

   - Visit [City Weather Checker](https://city-weather-checker-lrnj.onrender.com).

2. **Default city:**
   - If no city is provided, the default city "Dhaka" will be used.

## Project Setup

1. Clone the repository:
   git clone https://github.com/yourusername/city-weather-checker.git

2. Install dependencies:
   pip install -r requirements.txt

3. Set your OpenWeather API key in a .env file:
   API_KEY=your_openweathermap_api_key_here

4. Run the application locally:
   python app.py

## Technologies Used

1.  Flask: Web framework to build the web application.
2.  OpenWeather API: Provides current weather data.
3.  Waitress: WSGI server used for deployment.
