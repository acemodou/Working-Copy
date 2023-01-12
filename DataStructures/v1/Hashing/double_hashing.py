


def hash(key):
    return key % 10

def double_hash(key):
    '''
    Note: The 7 is the closest prime number to the size 
    of our array.
    '''
    return 7 - (key % 7)

def probe(HT, key):
    idx = hash(key)
    idx_2 = double_hash(key)
    i = 1
    while HT[(idx + i*idx_2) % 10] != 0:
        i += 1
    return (idx + i * idx_2) % 10

def insert(HT, key):
    """ Check if the hash index is not free probe for space and insert 
    the key in the available space"""
    
    idx = hash(key)

    if HT[idx] != 0:
        idx = probe(HT,key)
    HT[idx] = key

def search(HT, key):
   
    idx = hash(key)
    idx_2 = double_hash(key)
    i = 0
    while HT[(idx) % 10] != key:
        if i == 10:
            return "Not found "
        if i < 10:
            i += 1
        if HT[(idx + i*idx_2) % 10] == key:
            return (idx + i*idx_2) % 10
            
    return idx

if __name__ == "__main__":
    HT = [0] * 10
    insert(HT, 5)
    insert(HT, 25)
    insert(HT, 15)
    insert(HT, 35)
    insert(HT, 95)
    print(HT)
    
    print(search(HT, 25))
