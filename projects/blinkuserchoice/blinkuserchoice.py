#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os;

# Set board mode this means real counting the pins
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# Set pin 7 and 11 to accept output
GPIO.setup(7,GPIO.OUT)   # Red
GPIO.setup(11,GPIO.OUT)  # Green

try:

    os.system('clear')

    print "Which LED would you like to blink"
    print "1: Green?"
    print "2: Red?"

    led_choice = int(raw_input("Choose your option: "))
    times = int(raw_input("How many times: "))

    led = 11  # Default green
    if led_choice == 2:
        print 'red'
        led = 7
    else:
        led = 11

    for count in range(0, times):
        GPIO.output(led, GPIO.HIGH)

        # Wait a half second
        time.sleep(0.5)

        # Set pin to low meaning power off
        GPIO.output(led, GPIO.LOW)

        # Wait 1 second
        time.sleep(0.5)


finally:
    GPIO.cleanup()
