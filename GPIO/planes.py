import RPi.GPIO as GPIO
from time import sleep
import urllib.request, json, time

#GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

dumpurl = "http://localhost:8081/data.json"

while(True):
    with urllib.request.urlopen(dumpurl) as url:
        aircraft_json = json.loads(url.read().decode())
    
    count = len(aircraft_json)
    print(count)
    GPIO.output(17, count & 1 > 0)
    GPIO.output(27, count & 2 > 0)
    GPIO.output(22, count & 4 > 0)
    GPIO.output(23, count & 8 > 0)
    
