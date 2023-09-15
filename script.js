// js/script.js
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
