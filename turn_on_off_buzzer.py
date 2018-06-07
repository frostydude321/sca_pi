#!/usr/bin/env python
#this script will turn th buzzer on and off

import RPi.GPIO as GPIO
import time

#bread board setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for PAssive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set buzzer pins mode as output
GPIO.setup(buzz_pin, GPIO.OUT)

#create Buzz function and set inital sound frequancyto 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1000)

# change fre. and start buzzer useing buzz func. wiht 50% duty for 1 sec
Buzz.ChangeFrequency(3000)
Buzz.start(50)
time.sleep(1)
Buzz.stop()

#reset GPIO res. used by script
GPIO.cleanup()













