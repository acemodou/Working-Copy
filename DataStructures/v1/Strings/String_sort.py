def Sort(strs):
    N = len(strs)
    aux = [0] * N   
    msd_sort(strs, aux, 0, N-1, 0)
    return strs 

def msd_sort(strs, aux, lo, hi, d):
    if lo >= hi or d > len(strs[0]):
        return 0
    count =  [0] * 7
    for i in range(lo, hi+1):
        count[ord(strs[i][d]) -97 +1] +=1
    
    for i in range(len(count)-1):
        count[i+1] += count[i]
    
    for i in range(lo, hi+1):
        aux[count[ord(strs[i][d]) -97]] = strs[i]
        count[ord(strs[i][d]) -97] +=1
    
    for i in range(lo, hi+1):
        strs[i] = aux[i-lo]
    
    for i in range(len(count)-1):
        msd_sort(strs, aux, lo +count[i], lo +count[i+1]-1, d+1)


def LSD_sort(arr, w):
    
    for d in reversed(range(w)):
        aux = [0 for _ in arr]  
        
        # We choose 7 because we have 6 characters from A to F
        # We should choose 26 to cover all the letters in the alphabet
        count = [0] *7      
        
        # count the occurence of values
        for i in range(len(arr)):
            count[ord(arr[i][d]) -97 + 1] += 1 
        
        # cumulate the locations to know where the elements goes  
        
        for i in range(len(count)-1):
            count[i+1] += count[i]
        
        # Distribute records to their locations 
        for i in range(len(arr)):
            aux[count[ord(arr[i][d]) -97]] = arr[i]
            count[ord(arr[i][d])-97] +=1
        
        # Copy records back to their locations
        for i in range(len(aux)):
            arr[i] = aux[i]
    return arr 
            

def key_index_sort(strs):
    # Keep track of our count 
    count = [0 for _ in range(7)]

    # auxilary array to copy data
    aux = [0 for _ in range(len(strs))]

    # Strings are immutable and don't like to be overriden 

    res = ["" for _ in range(len(strs))]

    # Count frequency of occurence 
    for i in range(len(strs)):
        count[ord(strs[i]) -97 + 1] += 1
    
    # Cumulates tells us where the elements goes 
    for i in range(len(count)-1):
        count[i+1] += count[i]
    
    # Distribute records to their locations 
    for i in range(len(strs)):
        aux[count[ord(strs[i]) - 97]] = strs[i]
        count[ord(strs[i]) - 97] += 1
    
    # Copy in results since we can't mutate the original string
    for i in range(len(strs)):
        res[i] = aux[i]
    
    return res
def Sort_three_way(strs):
    three_way_sort(strs, 0, len(strs)-1, 0)
    return strs

def three_way_sort(strs, lo, hi, d):
    if lo >= hi or d > len(strs[0])-1:
        return 0
    lt, gt = lo, hi
    v = ord(strs[lo][d]) - 97
    i = lo + 1
    while i <= gt:
        t = ord(strs[i][d]) - 97
        if t < v:
            strs[lt], strs[i] = strs[i],strs[lt]
            lt +=1
            i += 1
        elif t > v:
            strs[i], strs[gt] = strs[gt],strs[i]
            gt -= 1
        else:
            i +=1
    three_way_sort(strs, lo, lt-1, d)
    if v >= 0:
        three_way_sort(strs, lt, gt, d+1)
    three_way_sort(strs, gt+1, hi, d)
