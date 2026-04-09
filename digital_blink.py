import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
state = 1
period = 1.0

GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)
