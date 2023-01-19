import heapq
def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'



def mergeKLists(lists):
    pass 
# def mergeKLists(lists):
#     pass 
   

        

        
    
simple_assert(mergeKLists([list1, list2, list3]), [1,1,2,3,4,4,5,6])
simple_assert(mergeKLists([]), None)


arrays = [[1, 5, 9, 21],[-1, 0],[-124, 81, 121],[3, 6, 12, 20, 150]]
simple_assert(mergeKLists(arrays),  [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])
