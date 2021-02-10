import os 
from os import path 
import shutil

def main():
    # make a duplicate of an existing file
    if path.exists('textfile.txt'):
        # get the path to the file in the current directory 
        src = path.realpath("textfile.txt")
        
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"

    # copy over the permission, modification times, and other info
    # If you want to copy the modification time and other metadata associated with the file, use copystat
    # shutil.copy(src, dst)
    # shutil.copystat(src, dst)

    # rename the original file
    os.rename('textfile.txt', 'newfile.txt')

if __name__ == "__main__":
    main()