import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
button = 13
state = 0
sleep_time = 0.2

GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    imp = GPIO.input(button)
    if imp:
        state = not state
        GPIO.output(led, state)

    time.sleep(sleep_time)
