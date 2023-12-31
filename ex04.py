import RPi.GPIO as GPIO
import time
import sys

Trig = 27
Echo = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

def read_distance():
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig, GPIO.LOW)

    while GPIO.input(Echo) == GPIO.LOW:
        sig_off = time.time()
    while GPIO.input(Echo) == GPIO.HIGH:
        sig_on = time.time()

    duration = sig_on - sig_off
    distance = duration * 34000 / 2
    return distance


print("distance=", int(read_distance()), "cm")
