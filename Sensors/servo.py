from gpiozero import Servo
from time import sleep

# Setup the servo on GPIO 4 (pin 7)
servo = Servo(17, min_pulse_width=0.0005, max_pulse_width=0.0025)

try:
    while True:
        # Move the servo to its maximum position
        servo.max()
        sleep(1)
        
        servo.mid()
        sleep(1)
        
        # Move the servo to its minimum position
        servo.min()
        sleep(1)
        
except KeyboardInterrupt:
    print("Program exited")
