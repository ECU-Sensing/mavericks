import time
import RPi.GPIO as GPIO

# Setup the GPIO pin for the buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(18, True)  # Turn on the buzzer
        time.sleep(0.5)        # Keep the buzzer on for 0.5 seconds
        GPIO.output(18, False) # Turn off the buzzer
        time.sleep(0.9)        # Wait for 1 seconds before the next buzz

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up the GPIO on CTRL+C exit
