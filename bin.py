import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

button_up = 9
button_down = 10
GPIO.setup(button_up, GPIO.IN)
GPIO.setup(button_down, GPIO.IN)


counter = 0

while True:
    counter += GPIO.input(button_up)
    counter -= GPIO.input(button_down)

    num = counter
    for i in range(8):
        GPIO.output(leds[i], num % 2)
        num /= 2
