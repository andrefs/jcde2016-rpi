# Blink LED
import RPi.GPIO as GPIO
from time import sleep

led=7

GPIO.setmode(GPIO.BOARD);
GPIO.setup(7, GPIO.OUT);

i=1;
while i<400:
	GPIO.output(7,True);  sleep(1);
	GPIO.output(7,False); sleep(1);

	i+=1;

GPIO.cleanup()

