from sort import Sorting
import pytest 


A = [3,7,9,10,6,5,12,4,11,2]
s1 = Sorting(A, 10)
expected = [2,3,4,5,6,7,9,10,11,12]

@pytest.mark.parametrize("test_input, expected",[
    (A, [2,3,4,5,6,7,9,10,11,12]),
    
])
def test_insertion_sort(test_input, expected):
    assert s1.insertion_sort(test_input) == expected

@pytest.mark.parametrize("test_input, expected",[
    (A, [2,3,4,5,6,7,9,10,11,12]),
])

def test_selection_sort(test_input, expected):
    assert s1.selection_sort(test_input) == expected

def test_bubble_sort():
    assert s1.bubble_sort(A) == expected

def test_adaptive_bubble_sort():
    assert s1.adaptive_bubble_sort(A) == True 
 
def test_quick_sort():
    assert s1.quick_sort(A, 0, len(A)-1) == expected

def test_merge_sort():
    assert s1.merge_sort(A, len(A)-1) == expected

def test_recursive_merge_sort():
    assert s1.recursive_merge_sort(A, 0, len(A)-1)

def test_count_sort():
    assert s1.count_sort(A) == expected

def test_shell_sort():
    assert s1.shell_sort(A) == expected

def test_bucket_sort():
    assert s1.bucket_sort(A) == expected

def test_radix_sort():
    assert s1.radix_sort(A) == expected 