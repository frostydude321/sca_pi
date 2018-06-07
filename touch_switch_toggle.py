#!/usr/bin/env python
#this script makesw the sensor go off

import RPi.GPIO as GPIO
import time

#beardboard setup
buzz_pin = 31

#set touch switch pins mode
GPIO.setup(touch_pin,GPIO.IN)

#loop that reads touch
while True :
          if GPIO.input(touch_pin) == 0 :
                    #add code to turn off a sensor
          if GPIO.input(touch_pin) == 1 :
                    # add code to turn on a sensor
