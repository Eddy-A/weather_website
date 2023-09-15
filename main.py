'''''
# Define the JavaScript code as a string
js_code = """
document.addEventListener('DOMContentLoaded', function () {
    const weatherForm = document.getElementById('weather-form');
    const weatherInfo = document.getElementById('weather-info');

    weatherForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const cityInput = document.getElementById('city');
        const countryInput = document.getElementById('country');

        // Get user inputs
        const city = cityInput.value;
        const country = countryInput.value;

        // Replace with your actual API key
        const apiKey = '2e4968960047575c008c2c656e51bcc9';

        // Construct the API URL
        const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${apiKey}`;

        // Fetch weather data
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Extract weather information
                const tempKelvin = data.main.temp;
                const tempFahrenheit = (tempKelvin - 273.15) * 9/5 + 32;
                const humidity = data.main.humidity;
                const windSpeed = data.wind.speed;

                // Display weather information
                weatherInfo.innerHTML = `
                    <h2>Weather in ${city}, ${country}</h2>
                    <p>Temperature: ${tempFahrenheit.toFixed(2)}°F</p>
                    <p>Humidity: ${humidity}%</p>
                    <p>Wind Speed: ${windSpeed} m/s</p>
                `;
            })
            .catch(error => {
                console.error('Error:', error);
                weatherInfo.innerHTML = '<p>Failed to fetch weather data.</p>';
            });
    });
});
"""

# Create an HTML file with the JavaScript code
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
</head>
<body>
    <div class="container">
        <h1>Weather App</h1>
        <form id="weather-form">
            <label for="city">City:</label>
            <input type="text" id="city" name="city" required>
            <label for="country">Country:</label>
            <input type="text" id="country" name="country" required>
            <button type="submit">Get Weather</button>
        </form>
        <div id="weather-info">
            <!-- Weather data will be displayed here -->
        </div>
    </div>
    <script>
        {js_code}
    </script>
</body>
</html>
"""

# Write the HTML code to a file
with open('index.html', 'w') as file:
    file.write(html_code)

# Open the HTML file in the default web browser
import webbrowser
webbrowser.open('index.html')
'''