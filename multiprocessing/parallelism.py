from PIL import Image, ImageFilter
import glob
import os

"""
Thumbnail size
"""
size_300 = (300, 300)

def get_images():
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            im = Image.open(filename)
            fn, fext = os.path.splitext(filename)
            im.thumbnail(size_300)
            im.save(f'size_300/{fn}_300{fext}')
            print(f'{fn + fext} was processed.')



def create_directory():
    pass

def process_images():
    pass


if __name__ == "__main__":
    get_images()

