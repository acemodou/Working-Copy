"""

Find the point of ration in a sorted rotated array
    1. find the miminum index in the array
    2. The number before the  minimum index of the array is the pivot
    3. The pivot will tell you how many times the array is rotated
    4. This can be done in O(n) by going through the entire array and compare every element
    5. Space complexity ?
    6. Can we do better ? Yes  step 7
    7. Sorted means we can search in O(log(n)) via binary search



"""


def find_min(A, n):
    return min(A)

def find_pivot(A, n):
    # basic way to grab pivot
     piv = find_min(A, n)
     piv1 = A.index(piv) -1
     return piv1, A[piv1]

def pivot(A, n):
    low = 0
    high = n-1
    while low < high:
        # if A[low] < A[high]:
        #     print('Array is not rotated. Ending Program ...')
        #     return A[low], A[high]
        mid = (low + high) //2
        before_pivot = (mid + n-1) % n
        after_pivot = (mid + 1) % n
        if A[mid] < A[after_pivot] and A[mid] < A[before_pivot]:
            return mid, A[mid]
        elif A[mid] > A[high]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def circularSortedArray(A, n, x):
    """
    Case 1: x = mid
    Case 2: Right half is sorted
        2.1 go searching in right sorted half
        2.2 Go search in the left
    Case 3: Left half is sorted
         3.1 : Go searching in the left sorted half
         3.2 Go search in the right
    """
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if x == A[mid]: return mid
        if A[mid] <= A[high]:
            if (x > A[mid]) and (x <= A[high]):
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (x < A[mid]) and (x >= A[low]):
                high = mid - 1
            else:
                low = mid + 1

    return -1

def sumCirularSortedArray(A, n , x):
    for i in range(len(A)):
        r = x - A[i]
        if r in A:
            print("There is a pair ( {}, {}) with sum {}".format(A[i], r, A[i] + r))
            return True

    print("There is no pair with sum {}. ".format(A[i] + r))
    return False

def pairInSortedRotatedArray(A, n, x):

    #find pivot element

    for i in range(0, n-1):
        if A[i] > A[i+1]:
            break


    l = (i + 1) % n # L is the index of the smallest element
    r = i # is the pivot

    while(l != r):

        if arr[l] + arr[r] == x:
            return True
        if arr[l] + arr[r] < x:
            l = (l + 1) % n
            print("Value of l is ", l)
        else:
            r = (n + r - 1)%n
            print("value of r is ", r)

    return False





if __name__ == "__main__":
    arr = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
    #print("The number of times rotated and the value: {} respectively".format(find_pivot(arr, 11)))
    #print("The number of times rotated and the value: {} respectively".format(pivot(arr, 11)))
    #print("The value of x is found in index : {} ".format(circularSortedArray(arr, 11, 22)))
    arr2 = [11, 15, 6, 8, 9, 10]
    n = len(arr2)
    #print("Output:  {}".format(sumCirularSortedArray(arr2, 5, 45)))
    print("Output:  {}".format(pairInSortedRotatedArray(arr2, n, 16)))


