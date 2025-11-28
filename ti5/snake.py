# Made by @Kacper Flak

from machine import Pin, SPI, ADC
from time import sleep_ms
import max7219
import random
from time import ticks_ms, ticks_diff

# voorbeeld code uit github
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(10)
display.set_rotation(90)


# lezen van de adc_value en aan de hand van de waarden de button's te verdelen
def read_keypad():

    KEYPAD_PIN = 26
    adc = ADC(Pin(KEYPAD_PIN))
    adc_value = adc.read_u16()
    # print(adc_value)

    if adc_value < 1500:
        return "SW1"
    elif adc_value < 15000:
        return "SW2"
    elif 32000 <= adc_value <= 33100:
        return "SW3"
    elif 49000 <= adc_value <= 50200:
        return "SW4"
    """
    TODO: SW5 toevoegen voor een game restart
    """


# food pixel op random plek op de matrix te spawnen, maar niet op de snake zelf
def food_spawn():
    while True:
        food_y = random.randint(0, 7)
        food_x = random.randint(0, 7)
        if food_x != snake_x and food_y != snake_y:
            # sleep_ms(100)
            return food_x, food_y


# hulp gekregen van AI om de food pixel te laten blinken
def draw_food(x, y):
    global food_visable
    global last_toggle
    global blink_rate

    now = ticks_ms()

    if ticks_diff(now, last_toggle) > blink_rate:
        food_visable = not food_visable
        last_toggle = now

    if food_visable:
        display.pixel(x, y, 1)


snake_x = 4
snake_y = 4

food_x, food_y = food_spawn()
food_visable = True
last_toggle = 0
blink_rate = 200

score = 0

led_1 = Pin(16, Pin.OUT)
led_2 = Pin(17, Pin.OUT)
led_3 = Pin(18, Pin.OUT)
led_4 = Pin(19, Pin.OUT)
led_5 = Pin(20, Pin.OUT)

# game loop
while True:

    display.fill(0)
    display.pixel(snake_x, snake_y, 1)
    draw_food(food_x, food_y)
    display.show()

    keypad = read_keypad()
    sleep_ms(100)

    # if statement hell
    if keypad == "SW1" and snake_x >= 0:
        # Als snake buiten de scherm komt wordt die verplaats naar de andere uit einde van de scherm op x en y
        # bijv bij x als snake_x == 7 (aan het rand dus) als ie nog een keer naar rechts gaat + 1 dan is (7 + 1) % 8 = 0 (de begin waarde)
        snake_x = (snake_x - 1) % 8
    elif keypad == "SW4" and snake_x <= 7:
        snake_x = (snake_x + 1) % 8
    elif keypad == "SW2" and snake_y >= 0:
        snake_y = (snake_y - 1) % 8
    elif keypad == "SW3" and snake_y <= 7:
        snake_y = (snake_y + 1) % 8

    # als snake zelfde positie heeft als food op y en x dan wordt de score met 1 verhoogd (ledje gaat aan) en wordt de food gerespawned weer op random locatie
    if food_x == snake_x and food_y == snake_y:
        food_x, food_y = food_spawn()
        score += 1

    if score >= 1:
        led_1.value(1)
    if score >= 2:
        led_2.value(1)
    if score >= 3:
        led_3.value(1)
    if score >= 4:
        led_4.value(1)
    if score >= 5:
        led_5.value(1)
        sleep_ms(2000)
        # als het einde is gaat led voor led uitzetten :)
        end = (
            led_5.value(0),
            sleep_ms(300),
            led_4.value(0),
            sleep_ms(300),
            led_3.value(0),
            sleep_ms(300),
            led_2.value(0),
            sleep_ms(300),
            led_1.value(0),
        )
        display.fill(0)
        display.show()
        break
