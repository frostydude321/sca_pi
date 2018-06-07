#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

x = random.randint(0,7)
y = random.randint(0,7)

sense.set_pixel(x, x, (0, 0, 255))
sense.set_pixel(y, y, (0, 0, 255))


time.sleep(0.1)
sense.clear()


