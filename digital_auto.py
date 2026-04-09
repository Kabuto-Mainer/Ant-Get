import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
foto_check = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(foto_check, GPIO.IN)

while True:
    imp = GPIO.input(foto_check)
    GPIO.output(led, not imp)

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
