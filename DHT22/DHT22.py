import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)
while True:
    try:
        temperature_c=dhtDevice.temperature
        tempareture_f=temperature_c*(9/5)+32
        humidity=dhtDevice.humidity
        print("Temp:{:.1f}F / {:.1f} C Humidity: {}%".format(tempareture_f, temperature_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

    except KeyboardInterrupt:
        dhtDevice.exit()
        print('exiting script')

    time.sleep(2.0)
