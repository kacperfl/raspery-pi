from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
while True:
    if btn.value() == 1:
        print("Button is in geclickt")
