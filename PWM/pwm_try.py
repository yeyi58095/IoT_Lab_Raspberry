#!/usr/bin/env python3
'''import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 12

GPIO.setup(12, GPIO.OUT)

freq = 1000
duty_cycle = 50
voltage_level = 2.5

pwm = GPIO.PWM(pin, freq)
high_time = duty_cycle / 100 * ( 1 / freq)
low_time =  (100 - duty_cycle) / 100 * (1 / freq)

high_voltage = voltage_level + ( 5 - voltage_level) * duty_cycle / 100
low_voltage = voltage_level - voltage_level * duty_cycle / 100

pwm.start(high_voltage / 5 * 100)

time.sleep()

pwm.ChangeDutyCycle(0)
pwm.ChangeDutyCycle(duty_cycle)

high_time = duty_cycle / 100 * ( 1 / freq)
low_time =  (100 - duty_cycle) / 100 * (1 / freq)

time.sleep(5)
pwm.stop()

GPIO.cleanup()
'''
''''
#!/usr/bin/env python3
import RPi.GPIO as IO 
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19, IO.OUT)
p = IO.PWM(19, 100)
p.start(0)

while True:
    for x in range(50):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)

    for x in range(50):
        p.ChangeDutyCycle(50 - x)
        time.sleep(0.1)
        
'''

from gpiozero import PWMLED
from time import sleep

led = PWMLED(19)

try:
    while True:
        for brightness in range(50):
            led.value = brightness / 100.0
            sleep(0.5)

        for brightness in range(50):
            led.value = (50 - brightness) / 100.0
            sleep(0.5)
except KeyboardInterrupt:
    led.off()

