const today_chart = document.getElementById("todayTemperatureLineChart");
const pointImageSunny = new Image(40, 40);
pointImageSunny.src = "./images/sun.png";
const pointImageThunderstorm = new Image(40, 40);
pointImageThunderstorm.src = "./images/thunderstorm.png";
const pointImageCloudy = new Image(40, 40);
pointImageCloudy.src = "./images/cloudy.png";
const pointImageHeavyRain = new Image(40, 40);
pointImageHeavyRain.src = "./images/heavy-rain.png";
const pointImageCloudComputing = new Image(40, 40);
pointImageCloudComputing.src = "./images/cloud.png";

new Chart(today_chart, {
  type: "line",
  data: {
    labels: [
      "08:00",
      "",
      "",
      "12:00",
      "",
      "",
      "16:00",
      "",
      "",
      "20:00",
      "",
      "",
      "00:00",
      "",
      "",
      "04:00",
    ],
    datasets: [
      {
        data: [28, 28, 29, 30, 31, 33, 34, 34, 33, 30, 29, 29, 27, 27, 27, 26],
        borderWidth: 1,
        fill: true,
        backgroundColor: "rgba(83,168,182,0.4)",
        borderColor: "#5585b5",
        tension: 0.5,
        pointHitRadius: 20,
      },
    ],
  },
  options: {
    scales: {
      y: {
        display: false,
        beginAtZero: true,
        max: 40,
        min: 10,
      },
    },
    plugins: {
      backgroundColor: {
        color: "",
      },
      legend: {
        display: false,
      },
    },
    animations: {
      radius: {
        duration: 400,
        easing: "linear",
        loop: (context) => context.active,
      },
    },
    elements: {
      point: {
        pointStyle: [
          "circle",
          pointImageSunny,
          "circle",
          pointImageSunny,
          "circle",
          pointImageSunny,
          "circle",
          pointImageSunny,
          "circle",
          pointImageCloudy,
          "circle",
          pointImageCloudy,
          "circle",
          pointImageCloudComputing,
          "circle",
          pointImageCloudComputing,
        ],
      },
    },
  },
});

const tomorrow_chart = document.getElementById("tomorrowTemperatureLineChart");

new Chart(tomorrow_chart, {
  type: "line",
  data: {
    labels: [
      "08:00",
      "",
      "",
      "12:00",
      "",
      "",
      "16:00",
      "",
      "",
      "20:00",
      "",
      "",
      "00:00",
      "",
      "",
      "04:00",
    ],
    datasets: [
      {
        data: [19, 20, 21, 21, 21, 21, 21, 21, 20, 20, 20, 19, 19, 18, 18, 16],
        borderWidth: 1,
        borderColor: "#5585b5",
        fill: true,
        backgroundColor: "rgba(83,168,182,0.4)",
        tension: 0.5,
        pointHitRadius: 20,
      },
    ],
  },
  options: {
    scales: {
      y: {
        display: false,
        beginAtZero: true,
        max: 40,
        min: 10,
      },
    },
    plugins: {
      backgroundColor: {
        color: "",
      },
      legend: {
        display: false,
      },
    },
    animations: {
      radius: {
        duration: 400,
        easing: "linear",
        loop: (context) => context.active,
      },
    },
    elements: {
      point: {
        pointStyle: [
          "circle",
          pointImageCloudComputing,
          "circle",
          pointImageThunderstorm,
          "circle",
          pointImageThunderstorm,
          "circle",
          pointImageHeavyRain,
          "circle",
          pointImageHeavyRain,
          "circle",
          pointImageHeavyRain,
          "circle",
          pointImageHeavyRain,
          "circle",
          pointImageHeavyRain,
        ],
      },
    },
  },
});
