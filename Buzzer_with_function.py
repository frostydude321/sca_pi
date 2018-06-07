#!/user/bin/env python
#htis turns the buzzer on and off using noise

import RPi.GPIO as GPIO
import time

#Beardboard set
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

#assign pin number for buzz; pin 32 = GPIO 12
buzz_pin = 32

#set buzz pins mode as output
GPIO.setup (buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM (buzz_pin,3000)

def buzz(freq):
       Buzz.ChangeFrequency (freq)
       Buzz.start (50)
       time.sleep (3)
       Buzz.stop ()

buzz (197.9)
buzz (197.9)
buzz (197.9)
buzz (182.4)
buzz (223.47)
buzz (197.9)

GPIO.cleanup ()
