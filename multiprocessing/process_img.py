import os
from PIL import Image, ImageFilter
import time

folder_path = 'C:/Users/mjaw/Desktop/Personal/gitBase/Working-Copy/Working-Copy/multiprocessing/pics'



def get_images():
    os.chdir('C:/Users/mjaw/Desktop/Personal/gitBase/Working-Copy/Working-Copy/multiprocessing/pics')
    img_names = ['photo-1493976040374-85c8e12f0c0e.jpg',
                 'photo-1504198453319-5ce911bafcde.jpg',
                 'photo-1513938709626-033611b8cc03.jpg',
                 'photo-1516117172878-fd2c41f4a759.jpg',
                 'photo-1516972810927-80185027ca84.jpg',
                 'photo-1522364723953-452d3431c267.jpg']

    return img_names


def create_dir(processed):
    os.chdir('C:/Users/mjaw/Desktop/Personal/gitBase/Working-Copy/Working-Copy/multiprocessing')
    if not os.path.exists(processed):
        os.mkdir(processed)


def processed_images(img_names):
    size = (1200, 1200)
    img = Image.open(img_names)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    create_dir("processed_img")
    img.save(f'processed_img/{img_names}')
    print(f'{img_names} was processed ...')


    img.save()

if __name__ == "__main__":
    #img_names = get_images()

    img_names = ['photo-1493976040374-85c8e12f0c0e.jpg',
                 'photo-1504198453319-5ce911bafcde.jpg',
                 'photo-1513938709626-033611b8cc03.jpg',
                 'photo-1516117172878-fd2c41f4a759.jpg',
                 'photo-1516972810927-80185027ca84.jpg',
                 'photo-1522364723953-452d3431c267.jpg']
    start = time.perf_counter()
    size = (1200, 1200)
    for img_name in img_names:
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))

        img.thumbnail(size)
        create_dir("processed_img")
        img.save(f'processed_img/{img_name}')
        print(f'{img_name} was processed ...')

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start , 2)} second(s)')




