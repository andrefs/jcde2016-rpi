# Turn LED on
import RPi.GPIO as GPIO

led=7

GPIO.setmode(GPIO.BOARD);
GPIO.setup(led, GPIO.OUT);

GPIO.output(led,True);

GPIO.cleanup()

