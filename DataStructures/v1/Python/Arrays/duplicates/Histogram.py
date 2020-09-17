
def makeHistogram(seq) -> dict:
    """
    take a list and returns a dictionary
    """
    hist ={}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

    # hist = [i for i in seq]
    # return hist

def listCounter(data, value):
    'S.count(value) -> integer -- return number of occurrences of value'
    return sum(1 for v in data if v is value or v == value)

def duplicate_count(data):
    """
    Count the number of duplicates
    """ 
    dupCount = 0
    
    #Loop through the data and increment counter 
    for i in range(len(data)):
        # if listCounter(data, data[i]) > 1:
        if data.count(i) > 1:
            dupCount +=1
    return dupCount

def checkIfDuplicates(data):
    ''' check if given list have duplicates '''
    if len(data) == len(set(data)):
        return 'There are no dups'
    else:
        return 'There are dups'

def checkDuplicates(data):
    '''
    Check if given list contains duplicates
    This ends once we found the first duplicate

    '''
    setOfElems = set()
    for elems in data:
        if elems in setOfElems:
            return 'There are dups'
        else:
            setOfElems.add(elems)
    return 'There are no dups'

def dupCountSort(data):
    #TODO: Sort the data 
    #TODO: start from the first index to the last 
    #TODO: check if the current index = prev index or next index 
    #TODO: Count first and last separately to avoid array bound errors 

    dupCount = 0
    data.sort()
    for i in range(1, len(data) - 1):
        if data[i] == data[i-1] or data[i] == data[i+1]:
            dupCount +=1

    'Count first and last separately to avoid array bound errors'
    if data[0] == data[1]:
        dupCount +=1
    if data[len(data) -1] == data[len(data) -2]:
        dupCount +=1

    return dupCount

def dupCountHalfCompare(data):
    #TODO: compare the two data and if a match is found 
    #TODO: Increment match 
    #TODO: Determine number duplicate based on matches
    #TODO: If there is a match increment dupCount by 2
    #TODO: If match is 1 increment dupCount by 1

    dupCount = 0
    for i in range(1, len(data)):
        match = 0
        for compare in range(i -1):
            if data[i] == data[compare]:
                match +=1

        if match == 1: 
            dupCount +=2
        if match > 1:
            dupCount +=1
            
    return dupCount




if __name__=="__main__":
    data = [20, 3, 19, 4, 14, 5, 12, 4, 3, 6, 1, 17, 8, 4, 6, 15, 1, 2, 7, 12]
    # print(f'Histogram duplicate count: {makeHistogram(data)} \n')
    #print(f'Histogram duplicate count: {duplicate_count(data)} \n')
    #print(f'Histogram duplicate count: {checkIfDuplicates(data)} \n')
    # print(f'Histogram duplicate count: {checkDuplicates(data)} \n')
    #print(f'Histogram duplicate count: {dupCountSort(data)} \n')
    print(f'Histogram duplicate count: {dupCountHalfCompare(data)} \n')