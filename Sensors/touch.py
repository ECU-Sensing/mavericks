import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin configuration
touch_pin = 17

# Set up the pin as an input
GPIO.setup(touch_pin, GPIO.IN)

try:
    while True:
        # Read the state of the touch sensor
        touch_state = GPIO.input(touch_pin)
        if touch_state == True:
            print("Touch detected!")
        else:
            print("No touch detected.")
        
        # Pause for a short period to debounce and reduce CPU usage
        time.sleep(0.1)
except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()
except:
    # Clean up GPIO on any other exit
    GPIO.cleanup()
