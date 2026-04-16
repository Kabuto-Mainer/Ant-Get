import r2_class as r2r
import sin_gen as sg
import time


if __name__ == "__main__":
    amplitude = 3.2
    signal_frequency = 10
    sampling_frequency = 1000
    t = 0.0

    try:
        dac = r2r.R2R_Dac([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)

        while True:
            # try:
                voltage = sg.get_sin_wave_ampltd(signal_frequency, t) * amplitude
                # voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
                t += 1 / sampling_frequency

            # except ValueError:
            #     print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
