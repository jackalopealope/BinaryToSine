import re
import numpy as np
import sounddevice as sd
import time

def filter_string(string):
    return re.sub(r"[^10]", "", string)

def play_sine_wave(bin_str):
    filtered_bin_str = filter_string(bin_str)

    one = 880
    zero = 440
    sample_rate = 44100
    duration = 0.1

    for char in filtered_bin_str:
        if char == '1':
            hz = one
        elif char == '0':
            hz = zero
        else:
            print("error")
            continue

        time_array = np.arange(0, duration, 1/sample_rate)
        sine_wave = np.sin(2 * np.pi * hz * time_array)
        sd.play(sine_wave, sample_rate)
        time.sleep(duration)

    sd.wait()

def main():
    bin_str = input("Str? ")
    play_sine_wave(bin_str)

if __name__ == '__main__':
    main()
