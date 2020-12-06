import zipfile
import shutil
import requests

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

r = requests.get('https://github.com/acemodou/OS/archive/master.zip')

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())
    data_zip.extractall('git_Dir')