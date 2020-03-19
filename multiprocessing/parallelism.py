from PIL import Image, ImageFilter
import glob
import os

file_path = '/Users/mjaw/Desktop/Personal/gitBase/Working-Copy/Working-Copy/multiprocessing/pics/*jpg'

def get_images(data_path):
    image_list = list()
    for filename in glob.glob(data_path):
        im = Image.open(filename)
        image_list.append(im)
        print(image_list)



def create_directory():
    pass

def process_images():
    pass


if __name__ == "__main__":
    pass

