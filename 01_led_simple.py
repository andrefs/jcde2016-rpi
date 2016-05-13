# Turn LED on
import RPi.GPIO as GPIO
from time import sleep

led=7

GPIO.setmode(GPIO.BOARD);
GPIO.setup(led, GPIO.OUT);

GPIO.output(led,True);
sleep(10);

GPIO.cleanup()

