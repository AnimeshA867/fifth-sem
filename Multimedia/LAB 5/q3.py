# Implement 1D DCT (discrete cosine transform) in python.

import numpy as np

def dct_1d(signal):
    N = len(signal)
    result = np.zeros(N)
    for k in range(N):
        sum_val = 0
        for n in range(N):
            sum_val += signal[n] * np.cos(np.pi * k * (2*n + 1) / (2 * N))
        result[k] = sum_val * np.sqrt(2 / N)
    result[0] *= np.sqrt(0.5)
    return result

# Example usage
signal = [1.0, 2.0, 3.0, 4.0]
dct_result = dct_1d(signal)
print(dct_result)
