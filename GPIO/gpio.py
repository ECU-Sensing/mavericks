import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 18 as an output
GPIO.setup(18, GPIO.OUT)

# Turn the LED on
GPIO.output(18, GPIO.HIGH)

# Wait for one second
time.sleep(1)

# Turn the LED off
GPIO.output(18, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()