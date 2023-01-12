import unittest
import sys
from unittest import result 
import strings
import String_sort


class TestStrings(unittest.TestCase):
    
    def test_stringstrings(self):
        result = strings.togglestrings('welcome')
        self.assertEqual(result, 'WELCOME')

    def test_revStrings(self):
        result = strings.revStrings('python')
        self.assertEqual(result, 'nohtyp')
    
    def test_palindrome(self):
        result = strings.palindrome('madam')
        self.assertEqual(result, 'Is Palindrome!')

    def test_stringDuplicates(self):
        result = strings.countDuplicates('finding')
        self.assertEqual(result, 'in')
    
    def test_bitwiseDuplicates(self):
        result = strings.bitwiseDuplicates('finding')
        self.assertEqual(result, 'in')
    
    def test_anagram(self):
        result = strings.anagram('decimal', 'medical')
        self.assertEqual(result, 'is anagram')

    def test_perm(self):
        str = list('abc')
        result = strings.perm(str, 0)
        self.assertIn(result, 'cba')
    
    def test_key_index_sort(self):
        arr = "dacffbdbfbea"
        ans = String_sort.key_index_sort(arr)
        self.assertEqual("".join(ans), "aabbbcddefff")

    
    def test_LSD_Sort(self):
        arr = ["dab", "cab", "fad","bad", "ebb", "ace", "add", "fed", "bed","fee","bee"]
        result = String_sort.LSD_sort(arr, 3)
        self.assertEqual(result, ["ace", "add",	"bad","bed","bee","cab","dab","ebb","fad","fed","fee"])
    
    def test_MSD_Sort(self):
        arr = ["dab", "cab", "fad","bad", "ebb", "ace", "add", "fed", "bed","fee","bee"]
        result = String_sort.Sort(arr)
        self.assertEqual(result, ["ace", "add",	"bad","bed","bee","cab","dab","ebb","fad","fed","fee"])
    
    def test_three_way_merge_Sort(self):
        arr = ["dab", "cab", "fad","bad", "ebb", "ace", "add", "fed", "bed","fee","bee"]
        result = String_sort.Sort_three_way(arr)
        self.assertEqual(result, ["ace", "add",	"bad","bed","bee","cab","dab","ebb","fad","fed","fee"])
    



if __name__ == '__main__':
    unittest.main()
