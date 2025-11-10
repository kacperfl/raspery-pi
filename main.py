from machine import Pin
import time


def blink_led(led, tijd_aan, tijd_uit):
    pin = Pin(20, Pin.OUT)

    while True:
        pin.value(1)
        time.sleep(0.5)
        pin.value(0)
        time.sleep(0.5)
