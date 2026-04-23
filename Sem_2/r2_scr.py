import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [16, 20, 21, 25, 26, 17, 27, 22]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

dynamic_range = 1.2

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    bits = decimal2binary(number)
    for i in range(8):
        GPIO.output(pins[i], bits[i])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()


