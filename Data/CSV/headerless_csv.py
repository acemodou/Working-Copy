import os 

'''
Step 1: 
TODO: Create Directory called headerRemoved 
TODO: Loop through each CSV 
TODO: validate the headers in a CSV to 
TODO: Remove headers in a CSV file in a current directory 
TODO: SKip any file that's not a CSV 
'''
_CSVDIRPATH = os.path.dirname(os.path.realpath(__file__))

def createDir(path):
    os.makedirs(path, exist_ok=True)
    print(f'Directory {path} created')



   

csv_headers = ['earthquake_id', 'occurred_on',]

validateCSVHeaders(csv_headers)

'''
Step 2: 
Read in the CSV file 
Store file in a list 
'''

'''
Step 3
write out the CSV file without the first row 
'''


'''
Once version one work. Make an improved version and use Dictionaries 
Compare this with validate header one 
'''