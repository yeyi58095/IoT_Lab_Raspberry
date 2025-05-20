#!/usr/bin/env python3
from gpiozero import PWMOutputDevice
from time import sleep

# Configuration
pin = 12  # BCM pin number
frequency = 1000  # Hz
duty_cycle_percent = 50  # Duty cycle as a percentage (0 to 100)

# Convert duty cycle to a 0.0 - 1.0 value
duty_cycle = duty_cycle_percent / 100.0

# Initialize PWMOutputDevice with given frequency and duty cycle
pwm = PWMOutputDevice(pin, frequency=frequency)
pwm.value = duty_cycle

# Keep PWM active for 5 seconds
sleep(5)

# Set duty cycle to 0 (turn off)
pwm.value = 0

# Note: gpiozero cleans up GPIO on exit
