import ic2 as r2r
import sin_gen as sg
import time


if __name__ == "__main__":
    amplitude = 5.0
    signal_frequency = 10
    sampling_frequency = 200
    t = 0.0

    try:
        dac = r2r.mcp_c(5.0, 0x61, False)

        while True:
            # try:
                voltage = sg.get_trig_wave_ampltd(signal_frequency, t) * amplitude
                # voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
                t += 1 / sampling_frequency

            # except ValueError:
            #     print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
