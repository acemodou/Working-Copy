import os
import csv
import json 

_CSVDIRPATH = os.path.dirname(os.path.realpath(__file__))
_READFILENAME = os.path.join(_CSVDIRPATH, 'earthquake.csv')
_WRITEFILENAME = os.path.join(_CSVDIRPATH, "headerRemoved")

def createDir(dir_name):
    os.makedirs(dir_name, exist_ok=True)
    print(f'Directory {dir_name} created')

def dir_exist(path):
    return os.path.exists(path)

def getDirName(dir_name):
    if not dir_exist(dir_name):
        try:
            createDir(dir_name)
        except FileExistsError:
            pass 
    else:
        print(f'{dir_name} name already exists')


def ValidateCSV(headers):
    csv_errors = list()
    for column in ["earthquake_id","occurred_on",]:
        if column not in headers:
            csv_errors.append(column)

    if csv_errors:
        raise ValueError("-E- Missng column in inventory: \n\t{}".format("\n\t".join(csv_errors)))

def searchCSV():
    '''
    Search for CSV files 
    return csvReader 
    '''
    for files in os.listdir(_CSVDIRPATH):
        if files.endswith(".csv"):
            csvFileObj = open(_READFILENAME, 'r')
            csvReader = csv.reader(csvFileObj)
            print('Removing header from: \n\t{}'.format(files))
    return csvReader

def readCSV():
    '''
    Read csv Files 
    Store rows without headers in csv 
    '''
    csvRows = []
    csvReader = searchCSV()
    for row in csvReader:
        if csvReader.line_num == 1:
            ValidateCSV(headers=row)
            continue
        csvRows.append(row)
    
    return csvRows

def writeCSV():
    '''
    Write headerless csv in a csv file called headerless earthquake
    store results in headerRemoved directory
    '''

    csvRows = readCSV()

    csvFileObj = open(os.path.join(_WRITEFILENAME, 'headerlessEarthquake.csv'), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for rows in csvRows:
        csvWriter.writerow(rows)
    csvFileObj.close()

def readTestLog():
    data = {}

    with open(os.path.join(_CSVDIRPATH, 'testlog.csv'), 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        y = 0
        for rows in csv_reader:
            data[y] = rows 
            y = y + 1

        with open(os.path.join(_CSVDIRPATH, 'newfile.json'), 'w') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
            
            
if __name__ =="__main__":
    readTestLog()

   
    
   
    
