def Parent(pos):
    return pos // 2

def left_child(pos):
    return 2 * pos

def right_child(pos):
    return (2 * pos) + 1

def Insert(A, n):
    i = n 
    temp = A[n]
    while i > 1 and temp > A[Parent(i)]:
        A[i] = A[Parent(i)]
        i = Parent(i)
    A[i] = temp 
        
def Delete(A, n):
    ele = A[1]
    A[1] = A[n]
    A[n] = ele 
    i = 1
    j = left_child(i)

    while j < n-1:
        if A[j] < A[j+1]:
            j += 1 

        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
            i = j 
            j = left_child(i)
        else:
            break 
    return A[n]

def max_heapify(A, pos):

    left_ch = left_child(pos)
    right_ch = right_child(pos)
    
    if left_ch <= len(A)-1 and A[left_ch] > A[pos]:
        largest = left_ch
    else:
        largest = pos 

    if right_ch <= len(A)-1 and A[right_ch] > A[pos]:
        largest = right_ch
    
    if largest != pos:
        A[largest], A[pos] = A[pos], A[largest]
        max_heapify(A, largest)

def build_max_heapify(A):
    n = len(A)-1
    for i in range(n // 2 , 0, -1):
        max_heapify(A, i)

def display(A):
    # Display the elements
    for i in range(1, len(A)):
        print(A[i], end=' ')
    print()

if __name__ == "__main__":
    # H = [0, 10, 20, 30, 25, 5, 40, 35]
    # for i in range(2, len(H)):
    #     Insert(H, i)
    
    # # Display the elements 
    # display(H)

    # # To do heapSort we can delete all the elements 1 by 1
    # for i in range(len(H)-1, 1, -1):
    #     Delete(H, i)

    # # Display elements
    # display(H) 
    
    Heapify = [0, 5, 10, 30, 20, 35, 40, 15]
    # How do we know how many iterations to build a complete max_heapify. Is it log(len(A))?
    for i in range(1, len(Heapify)-1):
        build_max_heapify(Heapify)
    display(Heapify)


