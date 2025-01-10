# Consider a sine wave with frequency 3hz, amplitude 1 and phase 0. Generate samples with sampling rate 2hz starting from 0sec to 10sec and plot the samples

import numpy as np
import matplotlib.pyplot as plt

# Sine wave parameters
freq = 3
amplitude = 1
phase = 0
sampling_rate = 2

# Generate time samples
time_continuous = np.arange(0, 10, 1/sampling_rate)
sine_wave_continuous = amplitude * np.sin(2 * np.pi * freq * time_continuous + phase)

# Plot the samples
plt.figure(figsize=(10, 4))
plt.plot(time_continuous, sine_wave_continuous, 'o-', label='Samples (2Hz)')
plt.title('Sine wave samples with sampling rate of 2Hz')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
