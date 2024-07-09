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
    + "&appid=5cf3a96718521eabbe985b47e198c8a9"
)


def reset_all():
    """Resets all pins to LOW"""
    GPIO.output(SUNNY_PIN, GPIO.LOW)
    GPIO.output(CLOUDY_PIN, GPIO.LOW)
    GPIO.output(RAINY_PIN, GPIO.LOW)
    GPIO.output(THUNDERSTORM_PIN, GPIO.LOW)


while True:

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content (which contains the weather data)
        data = response.json()
        description = data["weather"][0]["description"]

        print(description)

        reset_all()

        if description == "clear sky":
            GPIO.output(SUNNY_PIN, GPIO.HIGH)
        elif (
            description == "few clouds"
            or description == "scattered clouds"
            or description == "broken clouds"
        ):
            GPIO.output(CLOUDY_PIN, GPIO.HIGH)
        elif description == "shower rain" or description == "rain":
            GPIO.output(RAINY_PIN, GPIO.HIGH)
        elif description == "thunderstorm":
            GPIO.output(THUNDERSTORM_PIN, GPIO.HIGH)
        else:
            pass

    else:
        # Print an error message
        print("Error: Unable to fetch weather data.")

    time.sleep(600)
