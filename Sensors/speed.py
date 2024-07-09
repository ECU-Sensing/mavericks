import RPi.GPIO as GPIO
import time

# Pin Definitions
speed_sensor_pin = 18  # GPIO pin to receive speed sensor signal

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(speed_sensor_pin, GPIO.IN)
pulse_start_time = 0
pulse_count = 0

# Callback to handle pin state change
def sensor_callback(channel):
    global pulse_start_time, pulse_count
    if GPIO.input(speed_sensor_pin):  # Rising edge detected
        if pulse_start_time == 0:
            pulse_start_time = time.time()  # Record the start time of first pulse
        else:
            pulse_count += 1  # Increment pulse count

def calculate_speed():
    global pulse_start_time, pulse_count
    if pulse_count > 0:
        current_time = time.time()
        elapsed_time = current_time - pulse_start_time
        # Assuming 20 slots on the disc, adjust as necessary
        speed = (pulse_count / elapsed_time) * 30 / 20
        print(f"Speed: {speed} RPM")
        # Reset for next calculation
        pulse_start_time = current_time
        pulse_count = 0
    else:
        print("Waiting for more pulses")

# Interrupt setup
GPIO.add_event_detect(speed_sensor_pin, GPIO.RISING, callback=sensor_callback)

try:
    while True:
        calculate_speed()
        time.sleep(1)  # Adjust calculation period as necessary
except KeyboardInterrupt:
    GPIO.cleanup()
