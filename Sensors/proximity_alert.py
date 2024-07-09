import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 17  # Change this to your GPIO pin
ECHO = 18  # Change this to your GPIO pin
BUZZ = 22

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)

GPIO.output(TRIG, False)
GPIO.output(BUZZ, False)

def beep(duration_on, duration_off):
	GPIO.output(BUZZ, True)
	time.sleep(duration_on)
	GPIO.output(BUZZ, False)
	time.sleep(duration_off)

print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)  # 10us pulse
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Multiply by the speed of sound in cm/us
        distance = round(distance, 2)  # Round to two decimal places

        print(f"Distance: {distance}cm")
        
        if distance < 50:
            beep(0.5, 0.01)  # longer beeps for closer objects
        elif distance < 100:
            beep(0.05, 0.1)
        elif distance < 200:
            beep(0.05, 1)
        # else:
            # beep(0.4)  # Slower beeps for distant objects
        
        time.sleep(1)  # Delay to prevent constant pin toggling

except KeyboardInterrupt:
    GPIO.cleanup()  # Reset GPIO settings
