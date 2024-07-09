import RPi.GPIO as GPIO
import time

#GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    if GPIO.input(25):
        GPIO.output(13, True)
        GPIO.output(18, False)
        GPIO.output(21, True)

    else:
        GPIO.output(18, True)
        GPIO.output(21, True)
        GPIO.output(13, False)

