#!/usr/bin/env python

# Advanced - Manual Gain, High Resolution Example

import lgpio  #change1
import time
from ina219 import INA219
from ina219 import DeviceRangeError

# Set the constants that were calculated
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.8

# GPIO setup
RELAY_PIN = 18  # GPIO 18
h = lgpio.gpiochip_open(0)  # change2
lgpio.gpio_claim_output(h, RELAY_PIN)  # change3

def read_sensor():
    # Instantiate the ina object with the above constants
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address=0x40, busnum=1)
    # Configure the object with the expected bus voltage
    # (either up to 16V or up to 32V with .RANGE_32V)
    # Also, configure the gain to be GAIN_2_80MW for the above example
    ina.configure(ina.RANGE_16V, ina.GAIN_2_80MV)

    # Fixed bus voltage (9V)
    fixed_voltage = 9.0

    # Read current from INA219 (in mA)
    current_ma = ina.current()
    # Calculate power (in watts)
    power_watts = (fixed_voltage * current_ma) / 1000.0  # Convert mA to A and calculate power

    # Prints the values to the console
    print("Bus Voltage: %.3f V (fixed)" % fixed_voltage)
    try:
        print("Bus Current: %.3f mA" % current_ma)
        print("Power: %.3f W" % power_watts)
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        print("Current overflow:", e)

def relay_on():
    lgpio.gpio_write(h, RELAY_PIN, 1)  # change4
    print("Relay ON")

def relay_off():
    lgpio.gpio_write(h, RELAY_PIN, 0)  # change5
    print("Relay OFF")

if __name__ == "__main__":
    try:
        while True:
            print("Starting cycle...")
            relay_on()  # Step 1: Turn on relay
            time.sleep(1)
            read_sensor()  # Step 2: Read sensor data
            time.sleep(3)  # Step 3: Wait for 3 seconds
            relay_off()  # Step 4: Turn off relay
            time.sleep(1)
            read_sensor()  # Step 5: Read sensor data again
            print("Cycle completed. Waiting for next cycle...")
            time.sleep(3)  # Wait for 3 seconds between cycles
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        lgpio.gpiochip_close(h)  # change6