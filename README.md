Weather Clothing Suggestion
This is a simple web application that provides clothing suggestions based on the weather conditions of a given city.

Features
Retrieves weather data from the OpenWeatherMap API.

Displays the temperature in Fahrenheit.
Provides clothing suggestions based on the temperature range.
Shows a weather icon corresponding to the current weather condition.

Prerequisites
Python 3.x
Flask (Install using pip install flask)
Requests (Install using pip install requests)



Install the required dependencies (Flask and Requests).
Run the Flask application using the command python app.py.


Usage
Enter the name of a city in the provided input field.
Click the "Submit" button to retrieve the weather data for that city.
The temperature, clothing suggestion, and weather icon will be displayed.
If the temperature is 80°F or higher, an animation will be shown (for example, if it is hot).



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
        
The get_weather_data function retrieves weather data from the OpenWeatherMap API for a given city. It makes a GET request to the API and parses the JSON response. The temperature, weather condition, clothing suggestion, and weather icon class are extracted from the response and returned.


def get_clothing_suggestion(temperature):
    if temperature >= 80:
        return "It's hot. Wear a t-shirt and shorts or a summer dress."
    elif temperature >= 60:
        return "It's warm. Wear a light jacket or sweater."
    elif temperature >= 40:
        return "It's cool. Wear a jacket or coat."
    else:
        return "It's cold. Bundle up with warm clothing."
        
The get_clothing_suggestion function takes the temperature as input and returns a clothing suggestion based on the temperature range. The suggestions vary from wearing light clothing for hot temperatures to bundling up for cold temperatures.

