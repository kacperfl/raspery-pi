from machine import Pin
import time

pin = Pin(20, Pin.OUT)
def blink_led(led, tijd_aan, tijd_uit):
    while True:
        led.value(1)
        time.sleep(tijd_aan)
        led.value(0)
        time.sleep(tijd_uit)
        
blink_led(pin, 0.5, 0.5)

