import heapq
from heap_construction import Heap, MIN_HEAP

# def sortKSortedArray(array, k):
#     # Put the first k elements in our heap 
#     min_heap = []
#     for idx in range(min(k+1, len(array))):
#         heapq.heappush(min_heap , array[idx])
    
#     sorted_idx = 0
#     for idx in range(k+1, len(array)):
#         array[sorted_idx] = heapq.heappop(min_heap)
#         sorted_idx += 1
#         heapq.heappush(min_heap , array[idx])
#     while len(min_heap):
#         array[sorted_idx] = heapq.heappop(min_heap)
#         sorted_idx += 1
#     return array 


def sortKSortedArray(array, k):
    min_heap = Heap(array[: min(k+1, len(array))], MIN_HEAP)
    sorted_idx = 0
    for idx in range(k+1, len(array)):
        array[sorted_idx] = min_heap.remove()
        sorted_idx +=1 
        min_heap.insert(array[idx])
    
    while not min_heap.isEmpty():
        array[sorted_idx] = min_heap.remove()
        sorted_idx +=1
    return array 

    


    
