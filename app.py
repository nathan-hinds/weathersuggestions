from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "Your API Key"


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = round(data["main"]["temp"])
        weather_condition = data["weather"][0]["icon"]
        suggestion = get_clothing_suggestion(temperature)
        icon_class = get_weather_icon_class(weather_condition)

        return temperature, suggestion, icon_class
    else:
        return None, None, None


def get_clothing_suggestion(temperature):
    if temperature >= 80:
        return "It's hot. Wear a t-shirt and shorts or a summer dress."
    elif temperature >= 60:
        return "It's warm. Wear a light jacket or sweater."
    elif temperature >= 40:
        return "It's cool. Wear a jacket or coat."
    else:
        return "It's cold. Bundle up with warm clothing."


def get_weather_icon_class(weather_condition):
    icon_mapping = {
        "01d": "wi-day-sunny",
        "02d": "wi-day-cloudy",
        "03d": "wi-cloud",
        "04d": "wi-cloudy",
        "09d": "wi-showers",
        "10d": "wi-rain",
        "11d": "wi-thunderstorm",
        "13d": "wi-snow",
        "50d": "wi-fog"
    }

    return icon_mapping.get(weather_condition, "wi-na")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]

        temperature, suggestion, icon_class = get_weather_data(city)

        if temperature and suggestion:
            return render_template("index.html", temperature=temperature, suggestion=suggestion, icon_class=icon_class, city=city)
        else:
            error_message = "Unable to retrieve weather data. Please try again."
            return render_template("index.html", error_message=error_message)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
