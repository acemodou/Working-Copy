import heapq
def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'


# def mergeKLists(lists):
#     results = []
#     heap = []

#     for idx in range(len(lists)):
#         heap.append((lists[idx][0], idx, 0))
#     heapq.heapify(heap)

#     while heap:
#         val, row_idx, curr_pos = heapq.heappop(heap)
#         results.append(val)
#         curr_pos += 1
#         if curr_pos < len(lists[row_idx]):
#             heapq.heappush(heap, (lists[row_idx][curr_pos],row_idx, curr_pos))
#     return results 

        
# def mergeKLists(lists):
#     pass 
   
   
class LinkNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val 
        self.next = next 
    
    def addMany(self, values):
        current = self
        while current.next:
            current = current.next
        
        for val in values:
            current.next = LinkNode(val)
            current = current.next
        return self 


def mergeKLists(lists):
    heap = []
    output = []
    for idx, heads in enumerate(lists):
        heap.append((heads.val, idx))
    heapq.heapify(heap)

    while heap:
        val, idx = heapq.heappop(heap)
        output.append(val)
        lists[idx] = lists[idx].next 
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].val, idx))
    
    return output if len(lists) >=1 else None 

lists = [[1,4,5],[1,3,4],[2,6]]
list1 = LinkNode(1).addMany([4,5])
list2 = LinkNode(1).addMany([3,4])
list3 = LinkNode(2).addMany([6])

simple_assert(mergeKLists([list1, list2, list3]), [1,1,2,3,4,4,5,6])
simple_assert(mergeKLists([]), None)

#arrays = [[1, 5, 9, 21],[-1, 0],[-124, 81, 121],[3, 6, 12, 20, 150]]
#simple_assert(mergeKLists(arrays),  [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])
