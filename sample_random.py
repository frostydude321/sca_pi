import random
import RPi.GPIO as GPIO
import time
GPIO. setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(100)
random.seed(100)
n = random.randint(1,10)
#keep running until number is guessed
while True:
      guess = int(raw_input('Guess a number from 1 to 10:'))
      if guess < n:
          print"Guess is too low"
          Buzz.start(50)
          time.sleep(1)
          Buzz.stop()
      elif guess > n:
          print "Guess is too high"
          Buzz.start(50)
          time.sleep(1)
          Buzz.stop()
      else:
        print "you guessed right"
        GPIO.output(led_pin,True)
        time.sleep(2)
        GPIO.output(led_pin,False)
        break
        GPIO.cleanup ()
