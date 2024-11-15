from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city', '').strip()
    city = city or "Dhaka"
    
    weather_data = get_current_weather(city)

    if not weather_data or weather_data.get('cod') != 200:
        return render_template('cityNotFound.html')

    return render_template('weather.html',
                           title=weather_data["name"], 
                           status=weather_data["weather"][0]["description"].capitalize(),
                           temp=f"{weather_data['main']['temp']:.1f}",
                           feels_like=f"{weather_data['main']['feels_like']:.1f}")

if __name__ == '__main__':
    # Render uses the `$PORT` environment variable
    port = int(os.environ.get('PORT', 5000))
    serve(app, host='0.0.0.0', port=port)
