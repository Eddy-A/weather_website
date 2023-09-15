// Replace this line with your API URL
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${apiKey}`;

// Use a CORS proxy to fetch the data
const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
const finalUrl = proxyUrl + apiUrl;

// Fetch weather data
fetch(finalUrl)
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
