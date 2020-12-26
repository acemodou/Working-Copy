def missing_elements_naturalnumbers(arr):
    '''
    Find single missing element in sum of natural numbers
    n(n+1)/2 - sumOfElements in a list
    |1|2|3|4|5|6|8|9|10|11|12| -> Find the missing element in the sum of this natural list
    '''
    n = arr[-1]
    total = 0
    for i in range(len(arr)):
        total += arr[i]

    sum_of_Natural = (n * (n +1)) / 2
    return int(sum_of_Natural - total)

def single_missing_element(arr):
    '''
    Find single missing element in an ordered list
    |6|7|8|9|10|11|13|14|15|16|17|
    '''
    low = arr[0]
    diff = low - 0
    for i in range(len(arr)):
        if(arr[i] - i != diff):
            return f'The missing element is: {i + diff}'

def multiple_missing_elements(arr):
    '''
    Find multiple missing elements in an ordered list
    |6|7|8|9|11|12|13|14|15|17|18|
    '''
    low = arr[0]
    diff = low - 0
    for i in range(len(arr)):
        if(arr[i] - i != diff):
            print(i+diff)
            diff +=1
def multiple_missing_elements_unordered_list(arr):
    '''
    Find multiple missing elements in an unordered list
    Using Hashing/Bitset
    |3|7|4|9|12|6|1|11|2|10|
    '''
    low, high = min(arr), max(arr)
    bit_set = {}
    bit_set = dict.fromkeys(range(high),0)
    for i in range(len(arr)):
        bit_set[arr[i]] = bit_set.get(i, 0) + 1
    for key,values in bit_set.items():
        if values == 0 and key !=0:
            print(key)



if __name__ == "__main__":
    arr = [3,7,4,9,12,6,1,11,2,10]
    multiple_missing_elements_unordered_list(arr)
    # print(res)
   