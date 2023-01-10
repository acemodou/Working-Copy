


def hash(key):
    return key % 10

def probe(HT, key):
    idx = hash(key)
    i = 0
    while HT[(idx + i) % 10] != 0:
        i += 1
    return (idx + i) % 10


def insert(HT, key):
    """ Check if the hash index is not free probe for space and insert 
    the key in the available space"""
    
    idx = hash(key)

    if HT[idx] != 0:
        idx = probe(HT,key)
    HT[idx] = key

def search(HT, key):
    idx = hash(key)
    i = 0
    
    while HT[(idx + i) % 10] != key:
        if i == 10:
            return f"{key} : not found"
        i += 1
    return (idx + i) % 10

if __name__ == "__main__":
    HT = [0] * 10
    insert(HT, 26)
    insert(HT, 30)
    insert(HT, 45)
    insert(HT, 23)
    insert(HT, 25)
    print(HT)
    
    print(search(HT, 1))
