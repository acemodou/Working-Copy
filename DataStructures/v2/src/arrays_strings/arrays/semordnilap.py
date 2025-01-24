from validate_answers import simple_assert

def semordnilap(words):
    """ 
    Take the word: reversed it and check if the reverse is in the input
    store both: 
    Removed them from the input 
    """
    semordnilapPairs = []
    word_set = set(words)
    for word in words:
        reversed_word = "".join(reversed(word))
        if reversed_word in word_set and word != reversed_word:
            semordnilapPairs.append([word, reversed_word])
            word_set.remove(word)
            word_set.remove(reversed_word)
    return semordnilapPairs


input = ["desserts", "stressed", "hello"]
expected = [["desserts", "stressed"]]
actual = semordnilap(input)
simple_assert(actual, expected)
