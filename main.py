
import requests

class Weather():
    # Replace with your actual API key
    api_key = '2e4968960047575c008c2c656e51bcc9'
    
    def __init__(self):
        self.city = input("Enter the city: ")
        self.country = input("Enter the country: ")
        self.url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city},{self.country}&appid={self.api_key}'

    def api_request(self):
        # Make the API request
        response = requests.get(self.url)
        data = response.json()
        # Converting Kelvin to Fahrenheit
        temp_kelvin = data['main']['temp']
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return int(temp_fahrenheit), humidity, wind_speed

    def display(self):
        temp, humidity, wind_speed = self.api_request()
        print("Weather in", self.city, self.country)
        print("Temperature:", temp, "F")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "m/s")

    
# Create an instance of the Weather class
weather_instance = Weather()

# Display weather information
weather_instance.display()