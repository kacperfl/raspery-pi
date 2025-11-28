from machine import Pin
from utime import sleep_ms
led = Pin(20, Pin.OUT)
led.value(1) # LED aan
sleep_ms(2000)
led.value(0) # LED uit
