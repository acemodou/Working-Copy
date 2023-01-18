from typing import List

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def averageWaitingTime(customers: List[List[int]]) -> float:
    if len(customers) == 0:
        return 
    finish_time, waiting_time = 0, 0
    for arrival_time, prep_time in customers:
        finish_time = max((arrival_time + prep_time), (finish_time+prep_time))
        waiting_time += finish_time - arrival_time

    return round(waiting_time / len(customers), 5)


simple_assert(averageWaitingTime([[1,2],[2,5],[4,3]]), 5.00000)
simple_assert(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]), 3.25000)