import numpy
import time

def get_sin_wave_ampltd(freq: float, time: float):
    value = numpy.sin(2 * numpy.pi * freq * time)
    value += 1.0
    value /= 2.0
    # print(value)
    return value

def get_trig_wave_ampltd(freq: float, time: float):
    value = time * freq % 1.0

    if value <= 0.5:
        return value
    return value - 0.5

def wait_for_sampling_period(freq: float):
    time.sleep(1 / freq)

