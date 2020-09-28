def search_strings(str1, find_word, replace_word):
    # TODO: Go through the string 
    # TODO: find_word is in the string 
    # TODO: replace find_word with replace_word 
    new_str = str1.split()
    for i in new_str:
        if i.startswith(find_word):
            i = replace_word
        print(i, end=' ')


if __name__ == "__main__":
    search_strings("where is the film tonight", "film", "show")
