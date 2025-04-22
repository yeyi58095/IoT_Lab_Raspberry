import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
RED_PIN=5
YEL_PIN=6
GRN_PIN=13

GPIO.setup(RED_PIN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(YEL_PIN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(GRN_PIN,GPIO.OUT,initial=GPIO.LOW)

def TrafficLight(pin,duration):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin,GPIO.LOW)
try:
	while True:
		TrafficLight(RED_PIN,4);
		TrafficLight(YEL_PIN,2);
		TrafficLight(GRN_PIN,4);

except keyboardInterrupt:
	print("Except keyboardInterrupt")

finally:
	GPIO.cleanup()

