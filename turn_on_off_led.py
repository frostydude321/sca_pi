#!/usr/bin/env python
#this script turns the led on and off

import RPi.GPIO as GPIO
import time

#Breadboard setup
GPIO. setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for auto falsh led:pin 11 = GPIO 17
led_pin = 11

#set auto flash led pins mode as output
GPIO.setup(led_pin, GPIO.OUT)

# turn on led
GPIO.output(led_pin,True)
time.sleep(2)

# turn off led
GPIO.output(led_pin,False)

#reset GPIO resources used by script
GPIO.cleanup()
