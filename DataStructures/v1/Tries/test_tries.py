import unittest
from tries import Tries, NodeTries

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = Tries()
        words = ["wait", "waiter", "shop", "shopper"]
        for word in words:
            trie.add_word(word)
        
        self.assertEqual(trie.does_word_exist("wait"), True)
        self.assertEqual(trie.does_word_exist("waiter"), True)
        self.assertEqual(trie.does_word_exist("waite"), False)
        self.assertEqual(trie.does_word_exist("shop"), True)
        self.assertEqual(trie.does_word_exist("shopper"), True)
        self.assertEqual(trie.does_word_exist("shoppper"), False)
        self.assertEqual(trie.does_word_exist(""), True)
    
    def test_case_12(self):
        trie = NodeTries()
        words = ["wait", "waiter", "shop", "shopper"]
        for word in words:
            trie.add_word(word)
        
        self.assertEqual(trie.does_word_exist("wait"), True)
        self.assertEqual(trie.does_word_exist("waiter"), True)
        self.assertEqual(trie.does_word_exist("waite"), False)
        self.assertEqual(trie.does_word_exist("shop"), True)
        self.assertEqual(trie.does_word_exist("shopper"), True)
        self.assertEqual(trie.does_word_exist("shoppper"), False)
        self.assertEqual(trie.does_word_exist(""), True)

if __name__ == "__main__":
    unittest.main()
        
