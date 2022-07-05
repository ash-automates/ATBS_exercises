#! python3
#  getOpenWeather.py - Prints the weather for a location from the command line

import sys, pathlib, os, json, requests

# get an API key from openweathermap.org and save it to "OpenWeather-API.txt" in home folder
API_KEY = open(os.path.join(pathlib.Path.home(), "OpenWeather-API.txt")).read()

# Compute location from command line arguments & store it in a variable
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = " ".join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API

# TODO: Load JSON data into a Python variable
