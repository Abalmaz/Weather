function getCurrentDateTime() {
  let now = new Date();
  let months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  let weekDays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  let weekDay = weekDays[now.getDay()];
  let month = months[now.getMonth()];
  let date = now.getDate();
  let hours = now.getHours();
  let minutes = now.getMinutes();
  return `Today, ${month} ${date} from ${hours}:${minutes} <br> ${weekDay} `;
}

function celsiusToFahrenheit(celsius) {
  return Math.round(celsius * (9 / 5) + 32);
}

function fahrenheitToCelsius(fahrenheit) {
  return Math.round(((fahrenheit - 32) * 5) / 9);
}

let todayDate = document.querySelector("#today-date");
todayDate.innerHTML = getCurrentDateTime();

function updateUnitTemperature(event) {
  event.preventDefault();
  let currentUnit = document.querySelector(".active");
  let temperature = document.querySelector("#current-temperature");
  if (event.target.innerHTML === "°F") {
    let newTemperature = celsiusToFahrenheit(temperature.innerHTML);
    temperature.innerHTML = newTemperature;
    currentUnit.innerHTML = "°F";
    event.target.innerHTML = "°C";
  } else {
    let newTemperature = fahrenheitToCelsius(temperature.innerHTML);
    temperature.innerHTML = newTemperature;
    currentUnit.innerHTML = "°C";
    event.target.innerHTML = "°F";
  }
}

let updateUnit = document.querySelector("a.inactive");
updateUnit.addEventListener("click", updateUnitTemperature);
