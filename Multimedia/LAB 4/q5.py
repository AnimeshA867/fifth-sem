# Consider a sine wave with frequency 3hz, amplitude 1 and phase 0. Plot the sine wave starting from 0sec to 10sec. Consider Nyquist theorem for sampling.


import numpy as np
import matplotlib.pyplot as plt

# Sine wave parameters
freq = 3
amplitude = 1
phase = 0

# Nyquist sampling rate
nyquist_sampling_rate = 2 * freq

# Generate time samples
time_nyquist = np.arange(0, 10, 1/nyquist_sampling_rate)
sine_wave_nyquist = amplitude * np.sin(2 * np.pi * freq * time_nyquist + phase)

# Plot the sine wave
plt.figure(figsize=(10, 4))
plt.plot(time_nyquist, sine_wave_nyquist, 'o-', label='Samples (Nyquist)')
plt.title('Sine wave with Nyquist sampling rate')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
