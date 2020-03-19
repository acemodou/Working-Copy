from PIL import Image, ImageFilter
import os


if __name__ == "__main__":

   size_300 = (300, 300)
   size_700 = (700, 700)


   """
   Go through directories to check for files that end with .jpg.
   Save them as thumbnails of size 300 and 700
   change the file name to hace _300 for size 300 and _700 for size 700
   """
   for f in os.listdir('.'):
       if f.endswith('.jpg'):
           i = Image.open(f)
           fn, fext = os.path.splitext(f)
           i.thumbnail(size_300)
           i.save(f'size_300/{fn}_300{fext}')
