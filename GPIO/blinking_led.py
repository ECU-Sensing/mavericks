import RPi.GPIO as GPIO
import time

#GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

while True:
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(19, False)
    time.sleep(2)
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(19, True)
    time.sleep(2)
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(19, False)
    time.sleep(2)
    