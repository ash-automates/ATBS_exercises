#! python3
#  getOpenWeather.py - Prints the weather for a location from the command line

import sys, pathlib, os, json, requests

# get an API key from openweathermap.org and save it to "OpenWeather-API.txt" in home folder
API_KEY = open(os.path.join(pathlib.Path.home(), "OpenWeather-API.txt")).read()

# TODO: Compute location from command line arguments

# TODO: Download the JSON data from OpenWeatherMap.org's API

# TODO: Load JSON data into a Python variable
