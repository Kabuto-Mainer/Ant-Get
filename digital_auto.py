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

