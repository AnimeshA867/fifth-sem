# Plot the histogram of lenna.jpg. You can use matplotlib library.

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Load the image
lenna = io.imread('lenna.png')

# Plot the histogram
plt.figure(figsize=(10, 4))
plt.hist(lenna.ravel(), bins=256, color='gray', alpha=0.7)
plt.title('Histogram of lenna.jpg')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()
