#
# dht11 in https://pypi.org/project/dht11/
# pip install dht11
#

import RPi.GPIO as GPIO
import dht11

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin:=14)
result = instance.read()

print(result.is_valid())
print(f"T: {result.temperature:3.1f}C")
print(f"H: {result.humidity:3.1f}%")