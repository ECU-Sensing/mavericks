import adafruit_dht
import board
import time

# Setting up the sensor
# Replace 'D4' with the correct pin if your sensor is connected to a different GPIO pin.
sensor = adafruit_dht.DHT11(board.D4)

def read_humiture():
    try:
        # Read temperature and humidity
        temperature = sensor.temperature
        humidity = sensor.humidity

        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print("Failed to retrieve data from the humidity sensor")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

def main():
    while True:
        read_humiture()
        time.sleep(2)

if __name__ == "__main__":
    main()
