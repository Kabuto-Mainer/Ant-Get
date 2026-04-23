import time

import RPi.GPIO as GPIO


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.001, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(bit) for bit in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number

        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage

    def successive_approximation_adc(self):
        number = 0

        for bit in range(7, -1, -1):
            number += 2 ** bit
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                number -= 2 ** bit

        return number

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        voltage = number / 255 * self.dynamic_range
        return voltage


if name == "__main__":
    try:
        adc = R2R_ADC(3.3)

        while True:
            print(f"{adc.get_sar_voltage():.3f} В")

    finally:
        adc.deinit()
