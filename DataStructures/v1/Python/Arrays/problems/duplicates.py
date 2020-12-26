def findDuplicateElements(arr):
    '''
    Find duplicate elements and print the element just once
    '''
    if len(arr) == len(set(arr)):
        return f"There are no duplicates: {arr}"
    lastDuplicate = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] != lastDuplicate:
            print(arr[i])
            lastDuplicate = arr[i]

def countDuplicateElements(arr):
    '''
    Count duplicates 
    '''
    j = 0


    if len(arr) == len(set(arr)):
        return f"There are no duplicates: {arr}"
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1]:
            j = i+1
            while arr[i] == arr[j]:
                j +=1
            print(f'{arr[i]} is appearing {j - i} times')

def countDuplicateHashTable(arr):
    '''
    Count duplicates using bit set or hash table
    '''
    high = max(arr)
    hash_table = dict.fromkeys(range(high),0)
    for i in range(len(arr)):
        hash_table[arr[i]] = hash_table.get(i, 0) + 1
    for key, values in hash_table.items():
        if values > 1:
            print(f'{key} is appearing: {values} times')

def bruteForceFindPairSum(arr, k):
    '''
    a + b = k 
    '''
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                print(f'Pairs are {arr[i]} and {arr[j]}')

def findPairSum(arr, k):
    '''
    Assuming there are no negative values
    '''
    high = max(arr)
    hash_table = dict.fromkeys(range(high),0)
    for i in range(len(arr)):
        if hash_table[k - arr[i]] != 0 and hash_table[k - arr[i]] > 0:
            print(f'Pairs are {arr[i]} and  {k- arr[i]}')
        hash_table[arr[i]] = hash_table.get(i, 0) + 1

def findPairSumOrderedList(arr, k):
    '''
    Assuming our array is ordered
    '''
    i, j = 0, len(arr)-1
    while(i < j):
        if arr[i] + arr[j] == k:
            print(f'Pairs are {arr[i]} and  {arr[j]}')
            i +=1
            j -=1
        elif arr[i] + arr[j] > k:
            j -=1
        else:
            i +=1
            



if __name__ == "__main__":
    arr = [1,3,4,5,6,8,9,10,12,14]
    findPairSumOrderedList(arr, 10)