#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Set board mode this means real counting the pins
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# Set pin 7 to accept output
GPIO.setup(7,GPIO.OUT)

try:
    while(1):
        # Set pin 7 to HIGH this means power will flow
        GPIO.output(7, GPIO.HIGH)

        # Wait 1 second
        time.sleep(0.5)

        # Set pin to low meaning power off
        GPIO.output(7, GPIO.LOW)

        # Wait 1 second
        time.sleep(0.5)

finally:
    GPIO.cleanup()
