#A program to view a BMP file

from PIL import Image

def view_bmp(file_path):
    try:
        img = Image.open(file_path)
        img.show()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bmp_file = input("Enter the path to the BMP file: ")
    view_bmp(bmp_file)
