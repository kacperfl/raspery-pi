from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
btn = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
vorige_knop = 0
led_status = 0


while True:
    huidige_knop = btn.value()
    if huidige_knop == 1 and vorige_knop == 0:
        led_status = 1 - led_status
        led_pin.value(led_status)
    vorige_knop = huidige_knop
    time.sleep(0.1)
