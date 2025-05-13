#!/usr/bin/env python3
import smbus
import time

DEVICE = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07

CONTINUOUS_LOW_RES_MODE = 0x13
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
CONTINUOUS_HIGH_RES_MODE_2 = 0x11

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21
ONE_TIME_LOW_RES_MODE = 0x23

# bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def convertToNumber(data):
    result = (data[1] + (256 * data[0])) / 1.2
    return result

def readLight(addr=DEVICE):
    # Read data from I2C interface
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)


def main():
    while True:
        lightLevel =  readLight();
        print('Light Level : ' + format(lightLevel, '.2f') + "1x")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
