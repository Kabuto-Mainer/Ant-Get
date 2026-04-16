import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)


class R2R_Dac:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_num(self, number):
        if not (0 <= number <= 255):
            number = abs(number) % 255
            print("Число выходит за возможный диапазон значений")
            print(f"Использовано {number}")

        bits = decimal2binary(number)
        for i in range(8):
            GPIO.output(self.gpio_bits, bits)

    def set_voltage(self, volt):
        if not (0.0 <= volt <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            volt = 0.0

        self.set_num(int(volt / self.dynamic_range * 255))


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]



