# Write a program to convert lenna.jpg to gray and binary image. Do not use any library for conversion.

from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    return img

def save_image(image, output_path):
    image.save(output_path)

def grayscale(image):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Convert pixel to grayscale using luminance formula
            gray = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            image.putpixel((x, y), (gray, gray, gray))

def binarize(image, threshold=128):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Convert pixel to binary (black or white) based on threshold
            if pixel[0] < threshold:
                image.putpixel((x, y), (0, 0, 0))  # Black
            else:
                image.putpixel((x, y), (255, 255, 255))  # White

def main():
    input_image = "lenna.png"
    gray_output_image = "lenna_gray.jpg"
    binary_output_image = "lenna_binary.jpg"
    
    # Load the image
    image = load_image(input_image)
    
    # Convert to grayscale
    grayscale(image)
    # Save grayscale image
    save_image(image, gray_output_image)
    
    # Reload original image for binarization
    image = load_image(input_image)
    
    # Convert to binary
    binarize(image)
    # Save binary image
    save_image(image, binary_output_image)

if __name__ == "__main__":
    main()
