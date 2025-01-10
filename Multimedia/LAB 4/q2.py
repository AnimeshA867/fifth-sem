#Generate random NumPy array of size (400,400) in range [0,256) and save it as image.

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Generate random image
random_image = np.random.randint(0, 256, (400, 400), dtype=np.uint8)
io.imsave('random_image.png', random_image)

# Display the generated random image
plt.figure(figsize=(6, 6))
plt.imshow(random_image, cmap='gray')
plt.title('Randomly Generated Image')
plt.axis('off')
plt.show()
