import requests


def kelvinToC(temperature):
    return round(float(temperature - 273.15),2)



# Enter your API key here
# sample looks like 02a208ed61b2d8ae325a3661c1e3f1cf.
api_key = "Your API key"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()


if(x["cod"]==401):
    print("Invalid API keys, please check if your API key and ensure that it is activated.")
    print("In case you don't have an API key, sign up at https://openweathermap.org and check for API keys in accounts section.")
elif(x["cod"]==429):
    print("You exceeded the 60/min established limit of API calls. For more info https://openweathermap.org/faq#error401")
elif( x["cod"] == "404"):
    print("Invalid API call. Check the city name. Check at http://bulk.openweathermap.org/sample/")
else:
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    celsius = kelvinToC(current_temperature)
    z = x["weather"]
    weather_description = z[0]["description"]
    print(f"Weather report for {city_name}.\nSource: https://openweathermap.org")
    print(f"""
    Temperature (in K and in °C):\t\t{current_temperature} Kelvin / {celsius} °C
    Atmostpheric Pressure (in hPa unit):\t{current_pressure}
    Humidity (in percentage):\t\t\t{current_humidiy}
    Description : {weather_description.capitalize()}
    """)

