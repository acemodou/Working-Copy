from permuteUnique import *

def test_permute_unique():
    nums = [1,1,2]
    assert set_of_tuples_to_list(nums) == [[1,2,1],[2,1,1],[1,1,2]]

def test_permute_unique_strings():
    strs = ['A','A','B']
    assert set_of_tuples_to_list(strs) == [['A', 'A', 'B'],['B', 'A', 'A'],['A', 'B', 'A']]


def test_permute_unique():
    nums = [1,1,2]
    assert permute(nums) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

def test_permute_unique_strings():
    strs = ['A','A','B']
    assert permute(strs) == [['A', 'A', 'B'], ['A', 'B', 'A'], ['B', 'A', 'A']]