import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


class R2R_Dac:
    def __init__(self, gpio_bit, pwn_frec, dynamic_range, verbose = False):
        self.gpio_bit = gpio_bit
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bit, GPIO.OUT, initial = 0)
        self.shim = GPIO.PWM(gpio_bit, pwn_frec)
        self.shim.start(0.0)


    def deinit(self):
        GPIO.output(self.gpio_bit, 0)
        GPIO.cleanup()


    def set_voltage(self, volt):
        if not (0.0 <= volt <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            volt = 0.0

        duty = volt / self.dynamic_range * 100.0
        self.shim.ChangeDutyCycle(duty)


if __name__ == "__main__":
    try:
        dac = R2R_Dac(16, 200, 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()




