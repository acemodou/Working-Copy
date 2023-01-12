from typing import List

'''
Constraints:
1 <= N <= 1000
1 <= A[i] <= 10000

Solutions
1. Use built in method to reverse the array
2. Print the array starting from the last index
3. Use an auxillary array to copy the values in reverse order then print it.(Not efficient)
4. Swap first and last ... 

All solutions should be procedures since they don't return any value 
'''

def reverse_arr_1(arr:List[int]) -> None:
    print(' '.join(map(str, reversed(arr))))

def reverse_arr_2(arr:List[int]) -> None:
    print(' '.join(map(str, arr[::-1])))

def reverse_arr_3(arr:List[int]) -> None:
    '''
    Not efficient at all just for play 
    '''
    temp_arr = [elements for elements in arr[::-1]]
    print(''.join(map(str, temp_arr)))

def reverse_arr_4(arr:List[int]) -> None:
    first_index = 0
    last_index = len(arr)-1
    while last_index > first_index:
        arr[first_index], arr[last_index] = arr[last_index], arr[first_index]
        first_index += 1
        last_index -= 1
    print(' '.join(map(str, arr)))

def even_odd_Str():
    """
    Output:
    Hce akr
    Rn ak
    :return:
    """
    for _ in range(int(input('How many strings to input: '))):
        str = input()
        print(str[::2], str[1::2])

if __name__ == '__main__':
    # n = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))
    # if n >= 1 and n <= 1000 and len(arr) <= 10000:
    #     reverse_arr_4(arr)
    even_odd_Str()
      


  