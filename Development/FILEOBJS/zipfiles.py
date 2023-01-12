# import zipfile
import shutil
import requests
import os
from zipfile import ZipFile

# '''
# This is how we create a zip file
# '''
# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.txt')
#     my_zip.write('pic.jpg')

# '''
# This is how we unzip a file in python 
# '''
# with zipfile.ZipFile('files.zip', 'r', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.extract('files')

# shutil.make_archive('more_files', 'zip', 'files')
# shutil.unpack_archive('more_files.zip', 'amie')

# r = requests.get('https://github.com/acemodou/OS/archive/master.zip')

# with open('data.zip', 'wb') as f:
#     f.write(r.content)

# with zipfile.ZipFile('data.zip', 'r') as data_zip:
#     print(data_zip.namelist())
#     data_zip.extractall('git_Dir')

'''
Input: 
Input directory path
list of file extensions
output file path

Output:
Search input directory and all of it's directory 
For files with a specified extension 
Package them together into a zip file 

'''
def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                print(f'name:{name}, ext:{ext}')
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file), arcname=os.path.join(rel_path, file))


def unzip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'r') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                print(f'name:{name}, ext:{ext}')
                if ext.lower() in extension_list:
                    output_zip.extractall('logmine')


_SEARCH_DIR = os.path.dirname(os.path.realpath(__file__))

# zip_all(_SEARCH_DIR, ['.txt', '.jpg'], 'my_stuff.zip')

unzip_all(_SEARCH_DIR, ['.zip'], 'Ex_Files_Python_Code_Challenges.zip')