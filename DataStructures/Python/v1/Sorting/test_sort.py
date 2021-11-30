from sort import Sorting
import pytest 

A = [3,7,9,10,6,5,12,4,11,2]
s1 = Sorting(A, 10)

def test_selection_sort():
    assert s1.selection_sort(A) == [2,3,4,5,6,7,9,10,11,12]

def test_insertion_sort():
    assert s1.insertion_sort(A) == [2,3,4,5,6,7,9,10,11,12]

def test_bubble_sort():
    assert s1.bubble_sort(A) == [2,3,4,5,6,7,9,10,11,12]

def test_adaptive_bubble_sort():
    assert s1.adaptive_bubble_sort(A) == True 
 
def test_quick_sort():
    Qs = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3]
    assert s1.quick_sort(Qs, 0, len(Qs)-1) == [3, 5, 7, 9, 10, 11, 12, 13, 16, 24]
    