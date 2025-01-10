# Write a program to read lenna.jpg and crop width from 100 to 600 and height from 100 to 600 and display the image. Use NumPy library for cropping.

from PIL import Image
import numpy as np

def cropImage(input_image,output_image,x1,x2,y1,y2):
    image=Image.open(input_image);
    imageArray=np.array(image);

    croppedImage=imageArray[x1:x2,y1:y2];
    croppedImage=Image.fromarray(croppedImage);
    croppedImage.save(output_image);
    croppedImage.show();

def main():
    input_image='lenna.png';
    output_image='cropped.jpg';
    x1=100
    x2=600
    y1=100
    y2=600

    cropImage(input_image,output_image,x1,x2,y1,y2);

if __name__ == "__main__":
    main();
