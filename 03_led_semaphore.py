# Blink 3 LEDs in sequence
import RPi.GPIO as GPIO
from time import sleep

green=7
yellow=11
red=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green  , GPIO.OUT)
GPIO.setup(yellow , GPIO.OUT)
GPIO.setup(red    , GPIO.OUT)

i=1
while i<400:
	GPIO.output(green,True)
	sleep(4)
	GPIO.output(green,False)


	GPIO.output(yellow,True)
	sleep(1)
	GPIO.output(yellow,False)

	GPIO.output(red,True)
	sleep(3)
	GPIO.output(red,False)


	i+=1;

GPIO.cleanup()

