# Let us consider a sine wave with frequency 4400hz, 400m amplitude and phase 0. Generate sample from this sine wave at the rate of 44100hz for 1sec. Save the samples in the form of wave file in python. Use wave library.

import wave
import numpy as np

def generate_sine_wave(frequency, amplitude, phase, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return waveform

def save_wave(filename, waveform, sampling_rate):
    num_samples = len(waveform)
    with wave.open(filename, 'w') as wave_file:
        wave_file.setnchannels(1)  # mono
        wave_file.setsampwidth(2)  # 2 bytes (16 bits)
        wave_file.setframerate(sampling_rate)
        wave_file.writeframes((waveform.astype(np.int16)).tobytes())

# Parameters
frequency = 4400
amplitude = 400
phase = 0
sampling_rate = 44100
duration = 1

# Generate and save sine wave
waveform = generate_sine_wave(frequency, amplitude, phase, sampling_rate, duration)
save_wave('sine_wave.wav', waveform, sampling_rate)
