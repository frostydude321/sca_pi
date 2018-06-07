#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

y = (255, 255, 0)
b = (0, 0, 255)

speed = 0.02
message = "Waz up?"
while True:
    sense.show_message(message, speed, text_colour=y, back_colour=b)
    guess = raw_input("What is your guess?")
    if guess == message:
        print "YAY you did it!!!!"
        break
    else:
        speed = + 0.02

sense.clear()

