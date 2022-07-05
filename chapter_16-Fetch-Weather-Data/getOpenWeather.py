#! python3
#  getOpenWeather.py - Prints the weather for a location from the command line

import sys, pathlib, os, json, requests

# get an API key from openweathermap.org and save it to "OpenWeather-API.txt" in home folder
KEY = open(os.path.join(pathlib.Path.home(), "OpenWeather-API.txt")).read()

# Compute location from command line arguments & store it in a variable
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&APPID={KEY}"
res = requests.get(url)
res.raise_for_status()

# Load JSON data into a variable & Print weather descriptions into terminal
weather_data = json.loads(res.text)
w = weather_data["list"]

print("Current weather in %s:" % (location))
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])
