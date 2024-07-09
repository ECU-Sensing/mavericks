from PIL import Image
import pyautogui
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    # Load the image to be detected
    image_to_detect = Image.open('/home/pi/Downloads/image_to_detect.png')

    # Get the screen size
    screen_size = pyautogui.size()

    location = None

    # Search for the image on the screen
    location = pyautogui.locateOnScreen(image_to_detect, confidence=0.8)

    # Check if the image was found
    if location is not None:
        GPIO.output(18, True)
        time.sleep(.025)
        GPIO.output(18, False)
        time.sleep(.025)

        
        # Print the location of the image on the screen
        # print(f"Image found at: {location}")
        
        # # Get the center of the image location
        # center = pyautogui.center(location)
        # 
        # # Move the mouse cursor to the center of the image location
        # pyautogui.moveTo(center)
    else:
        # Print a message indicating that the image was not found
        GPIO.output(19, True)
        time.sleep(.025)
        GPIO.output(19, False)
        time.sleep(.025)

