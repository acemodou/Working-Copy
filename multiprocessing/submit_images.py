import os
from PIL import Image, ImageFilter
import time
import concurrent.futures

directory_path = 'C:/Users/mjaw/Desktop/Personal/'
path = 'gitBase/Working-Copy/Working-Copy/multiprocessing/pics'
file_path = os.path.join(directory_path, path)

size_300 = (300, 300)

mode = 0o666


def make_directory_with_mode(directory, mode):
    if not os.path.exists(directory):
        os.mkdir(directory, mode)


def get_images():
    os.chdir(file_path)
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            im = Image.open(filename)
            im = im.filter(ImageFilter.GaussianBlur(15))
            fn, fext = os.path.splitext(filename)
            make_directory_with_mode('size_300', mode)
            im.thumbnail(size_300)
            im.save(f'size_300/{fn}_300{fext}')
            print(f'{fn + fext} was processed.')

def process_images():

    """
    We use concurrent futures because it has a simpler interface
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(get_images)


if __name__ == "__main__":

    start = time.perf_counter()

    process_images()

    finish = time.perf_counter()

    print(F'Finished in {round(finish - start, 2)} second(s)')






