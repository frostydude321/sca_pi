#!/usr/bin/python
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
yellow = (255, 255, 0)
blue = (0, 0, 255)

speed = 0.02

message = ("Never gonna give you up, never gonna let you down, never gonna run around and desert you...")

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear
