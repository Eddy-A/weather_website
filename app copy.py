from flask import Flask, render_template, request
import requests

app = Flask(__name__)

class Weather():
    api_key = '2e4968960047575c008c2c656e51bcc9'

    def api_request(self, city, country):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return int(temp_fahrenheit), humidity, wind_speed

@app.route('/')
def index():
    return render_template('weather_form.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    country = request.form['country']
    weather_instance = Weather()
    temp, humidity, wind_speed = weather_instance.api_request(city, country)
    return render_template('weather.html', city=city, country=country, temp=temp, humidity=humidity, wind_speed=wind_speed)

if __name__ == '__main__':
    app.run(debug=True)