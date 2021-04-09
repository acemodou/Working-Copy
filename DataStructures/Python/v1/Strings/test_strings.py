import unittest
import sys
from unittest import result 
import strings


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
    



if __name__ == '__main__':
    unittest.main()


