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
    flag_1 = GPIO.input(button_up)
    flag_2 = GPIO.input(button_down)

    if flag_1 + flag_2 == 2:
        counter = 255
    else:
        counter += flag_1
        counter -= flag_2
    time.sleep(0.05)
    counter = max(0, min(counter, 255))

    num = counter
    for i in range(8):
        val = num % 2
        GPIO.output(leds[i], val)
        num //= 2
    
