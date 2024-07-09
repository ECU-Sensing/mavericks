import RPi.GPIO as GPIO
import time
import requests

# Set up GPIO pins
SUNNY_PIN = 11
CLOUDY_PIN = 13
RAINY_PIN = 15
THUNDERSTORM_PIN = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SUNNY_PIN, GPIO.OUT)
GPIO.setup(CLOUDY_PIN, GPIO.OUT)
GPIO.setup(RAINY_PIN, GPIO.OUT)
GPIO.setup(THUNDERSTORM_PIN, GPIO.OUT)


# Make an API request to the OpenWeatherMap API
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q="
    + input("City: ")
    + "&appid=API_ID"
)


def reset_all():
    """Resets all pins to LOW"""
    GPIO.output(SUNNY_PIN, GPIO.LOW)
    GPIO.output(CLOUDY_PIN, GPIO.LOW)
    GPIO.output(RAINY_PIN, GPIO.LOW)
    GPIO.output(THUNDERSTORM_PIN, GPIO.LOW)


while True:
    time.sleep(1)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content (which contains the weather data)
        data = response.json()
        description = data["weather"][0]["description"]

        print(description)

        reset_all()

        # Insert conditional statements here to light up the correct LED for the weather
        # clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow, mist

    else:
        # Print an error message
        print("Error: Unable to fetch weather data.")
