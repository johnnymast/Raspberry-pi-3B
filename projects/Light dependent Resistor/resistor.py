import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin = 4

GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)

DEBUG = 1

print("-------------------------")
print(" Light depended Resistor ")
print("-------------------------")


def ReadSensor(Pin):
    reading = 0
    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, GPIO.LOW)
    time.sleep(.1)

    GPIO.setup(Pin, GPIO.IN)

    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(Pin) == GPIO.LOW):
        reading += 1
    return reading


while True:
    print ReadSensor(pin)
    time.sleep(1)

GPIO.clear();

