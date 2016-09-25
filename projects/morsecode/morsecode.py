import RPi.GPIO as GPIO
import Morse
import time

# Set board mode this means real counting the pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# Set pin 7 to accept output
GPIO.setup(7,GPIO.OUT)

message = raw_input("What message do you want to broadcast? ")

morse_code = Morse.encode(message)

for char in morse_code.split(' '):
    for symbol in char:
        if symbol == '.':
            GPIO.output(7, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(7, GPIO.LOW)
            time.sleep(.1)
        elif symbol == '-':
            GPIO.output(7, GPIO.HIGH)
            time.sleep(.2)
            GPIO.output(7, GPIO.LOW)
            time.sleep(.2)

GPIO.cleanup()