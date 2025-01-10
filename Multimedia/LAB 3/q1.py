#Write a program to read lenna.jpg. Convert it into png and tif. Display disk size of jpg, png, and tif. Display the actual size of jpg without using any library.

from PIL import Image
import os

def convert_image(input_path, output_format):
    image = Image.open(input_path)
    output_path = os.path.splitext(input_path)[0] + '.' + output_format
    image.save(output_path)
    return output_path

def get_file_size(file_path):
    return os.path.getsize(file_path)

def main():
    input_image = "lenna.png"
    
    # Convert to PNG
    png_image = convert_image(input_image, "png")
    png_size = get_file_size(png_image)
    
    # Convert to TIFF
    tiff_image = convert_image(input_image, "tif")
    tiff_size = get_file_size(tiff_image)
    
    # Get JPG file size
    jpg_size = get_file_size(input_image)
    
    print("JPEG size:", jpg_size, "bytes")
    print("PNG size:", png_size, "bytes")
    print("TIFF size:", tiff_size, "bytes")

if __name__ == "__main__":
    main()
