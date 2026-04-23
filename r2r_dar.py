import RPi.GPIO as GPIO


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def destroy(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def num_to_dac(self,  num):
        max_value = 2 ** len(self.bits_gpio) - 1;
        if not 0 <= number <= max_value:
            print(f"Число должно быть в диапазоне 0..{max_value}")
            num = num % max_value

        bits = [int(bit) for bit in f"{number:0{len(self.bits_gpio)}b}"]
        GPIO.output(self.bits_gpio, bits)

        if self.verbose:
            print(f"DAC <= {number:3d} | bits = {bits}")

    def sequential_counting_adc(self):
        max_value = 2 ** len(self.bits_gpio) - 1;
        for number in range(max_value + 1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            comp_value = GPIO.input(self.comp_gpio)

            if self.verbose:
                print(f"number = {number:3d}, comp = {comp_value}")

            if comp_value == 0:
                return number

        return max_value

    def get_sc_voltage(self):
        max_value = 2 ** len(self.bits_gpio) - 1;
        digital_value = self.sequential_counting_adc()
        voltage = digital_value / max_value * self.dynamic_range

        if self.verbose:
            print(f"ADC code = {digital_value}, voltage = {voltage:.3f} V")

        return voltage


try:
    adc = R2R_ADC(dynamic_range=3.3, compare_time=0.01, verbose=False)

    while True:
        voltage = adc.get_sc_voltage()
        print(f"{voltage:.3f} V")
        time.sleep(0.1)

finally:
    if adc is not None:
        adc.destroy()
