import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
pin = 7

GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(pin)
while True:
   if ( GPIO.input(pin) == False ):
      print("Button Pressed")
      os.system('date')
      print GPIO.input(pin)
      time.sleep(5)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)