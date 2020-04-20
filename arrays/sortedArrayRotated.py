


def findMinimumIndex(A,n):
    min = A[0]
    min_index = 0

    for i in range(0,len(A)):
        if(A[i] < min):
            min = A[i]
            min_index = i
    return min_index





if __name__ == "__main__":
    arr = [15,22,23,28,31,38,5,6,8,10,12]
    print("The number of times rotated and the value: {} respectively".format(findpivot(arr,11)))




