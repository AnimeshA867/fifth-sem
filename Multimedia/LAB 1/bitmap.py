import numpy as np
from PIL import Image

def main():
    try:
        with open("F4.bmp", "rb") as p:
            # Skip the first 436 bytes (header)
            p.seek(436)
            
            # Initialize the image
            img = np.zeros((480, 640), dtype=np.uint8)
            
            # Read the pixel data and plot them
            x, y = 0, 479
            while True:
                c = p.read(1)
                if not c:
                    break
                i = ord(c)
                img[y, x] = i
                x += 1
                if x >= 640:
                    x = 0
                    y -= 1
    
        # Display the image
        image = Image.fromarray(img)
        image.show()
        
        # Wait for user input
        input("Press Enter to exit...")
    
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()

