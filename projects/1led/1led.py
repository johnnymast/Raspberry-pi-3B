#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Set board mode this means real counting the pins
GPIO.setmode(GPIO.BOARD)

# Set pin 7 to accept output
GPIO.setup(7,GPIO.OUT)

print "Lights on " + str(GPIO.HIGH)

# Set pin 7 to HIGH this means power will flow
GPIO.output(7, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

print "Lights off"

# Set pin to low meaning power off
GPIO.output(7,GPIO.LOW)

# Clean up
GPIO.cleanup()