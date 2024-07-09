import RPi.GPIO as GPIO
import time

# Pin Definitions
sensor_pin = 17  # GPIO pin connected to the sensor OUT pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(sensor_pin, GPIO.IN)  # Sensor pin set as input

try:
    while True:
        if GPIO.input(sensor_pin):
            print("No obstacle detected.")
        else:
            print("Obstacle detected!")
        time.sleep(0.1)  # Sleep for 100 milliseconds

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()  # Clean up GPIO settings
