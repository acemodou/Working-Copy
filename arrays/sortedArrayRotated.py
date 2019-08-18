"""Find the point of ration in a sorted rotated array
    #1. find the miminum index in the array
    #2. The minimum index of the array is the pivot
    #3. The pivot will tell you how many times the array is rotated
    #4. This can be done in O(n) by going through the entire array and compare every element
    #5. Space complexity ?
    #6. Can we do better ?"""


def findMinimumIndex(A,n):
    min = A[0]
    min_index = 0

    for i in range(0,len(A)):
        if(A[i] < min):
            min = A[i]
            min_index = i
    return  min_index

#assuming the array is not A[1]

def findpivot(A,n):
    low = 0
    high = n-1

    while(low < high):
        if A[low] < A[high]:
            return low, A[low]
        mid = (low + high) //2
        afterpivot = (mid + 1) % n
        beforepivot = (mid + n-1) % n
        if A[mid] < A[afterpivot] and A[mid] < A[beforepivot]:
            return mid, A[mid]
        elif A[mid] > A[high]:
            low = mid + 1
        else:
            high = mid -1
    return -1


if __name__ == "__main__":
    arr = [15,22,23,28,31,38,5,6,8,10,12]
    print("The number of times rotated and the value: {} respectively".format(findpivot(arr,11)))




