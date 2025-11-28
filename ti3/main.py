from machine import Pin, ADC
from utime import sleep_ms

adc = ADC(Pin(26))

while True:
    val = adc.read_u16()
    print(val)
    sleep_ms(500)


# from machine import Pin, ADC
# from utime import sleep_ms
# adc = ADC(Pin(26))
# while True:
# val = adc.read_u16()
# print(val)
# sleep_ms(1000)
