function capitalize(string) {
  let capitalizeFirstLetter = string[0].toUpperCase();
  return capitalizeFirstLetter + string.slice(1);
}

function displayWeather(response) {
  let temperature = Math.round(response.data.temperature.current);
  let city_name = response.data.city;

  if (city_name && temperature) {
    updateCurrentCity(city_name);
    updateCurrentTemperature(temperature);
  } else {
    alert(
      `Sorry, we don't know the weather for this city, try going to https://www.google.com/search?q=weather+${city_name}`
    );
  }
}

let searchButton = document.querySelector("#search-button");
let inputCity = document.querySelector("#input-city");
searchButton.addEventListener("click", handleInput);
inputCity.addEventListener("keyup", (event) => {
  if (event.key === "Enter") {
    handleInput(event);
  }
});

let apiKey = config.WEATHER_API_KEY

function handleInput(event) {
  event.preventDefault();
  let city_name = document.querySelector("#input-city").value;
  let url = `https://api.shecodes.io/weather/v1/current?query=${city_name}&key=${apiKey}&units=metric`;
  axios.get(url).then(displayWeather);
}

function updateCurrentCity(cityName) {
  let currentCity = document.querySelector("#current-city");
  currentCity.innerHTML = cityName;
}

function updateCurrentTemperature(currentTemperature) {
  let temperature = document.querySelector("#current-temperature");
  temperature.innerHTML = currentTemperature;
}
