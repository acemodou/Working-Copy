from heapq import heapify, heappop
from typing import List

def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'
    
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = frequecyOfOccurence(nums)
    heap = [(-freq, num) for num, freq in count.items()]
    heapify(heap)

    output = []
    for _ in range(k):
        output.append(heappop(heap)[1])
    return output 

def frequecyOfOccurence(nums):
    freq = {}
    for val in nums:
        freq[val] = freq.get(val, 0) + 1
    return freq 

simple_assert(topKFrequent([1,1,1,2,2,3], 2), [1,2])
simple_assert(topKFrequent([1], 1), [1])
