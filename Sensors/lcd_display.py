import sys
from RPLCD.i2c import CharLCD
import time

# Set up the LCD display
lcd = CharLCD('PCF8574', 0x27)

def display_message(message):
    lcd.clear()
    lcd.write_string(message[:16])  # Display only the first 16 characters
    lcd.crlf()  # Move cursor to next line
    if len(message) > 16:
        lcd.write_string(message[16:32])  # Display next 16 characters on the second line
    time.sleep(5)  # Display the message for 5 seconds
    lcd.clear()  # Clear the display after showing the message

def main():
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "Hello, World!"
    display_message(message)

if __name__ == '__main__':
    main()
