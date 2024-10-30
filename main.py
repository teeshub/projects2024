import argparse
import pyfiglet
from simple_chalk import chalk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
# environment variables
print("!**************** Weather Report ****************!")

# API key for Openweathermap
API_KEY = os.getenv("API_KEY")

# Base URL for Openweathermap API 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Map the weather codes to weather icons
WEATHER_ICONS = {

    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

# I use the argparse library to parse the command-line arguments. The program expects 
# one argument, the country to check the weather for.
# Parse command-line arguments

parser = argparse.ArgumentParser(description="Check the weather for a certain country/city.")
parser.add_argument("country", help="the country/city to check the weather for")
args = parser.parse_args()

# Construct the API URL with the query parameters using.
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make the API request using the requests module.
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information."))
    exit()

#Parsing the JSON response from the API and extraxt the weather information.
data = response.json()


# Parse the JSON response from the API and extract the weather information
# (temperature, feels like temperature, description, icon, city, and country).

# Get weather information from response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct the output with the weather icons
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print the output
print(chalk.green(output))
# print(output)
