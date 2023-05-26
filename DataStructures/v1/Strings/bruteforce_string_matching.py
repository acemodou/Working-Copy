import pytest


def bruteforce_string_search(string : str, substring : str) -> bool:
    # Write your code here.
    if len(string) < len(substring):
        return False
    N = len(string)
    M = len(substring)

    for i in range(N-M +1):
        j = 0
        while j < M and string[i+j] == substring[j]:
            j += 1
        if j == M:
            return True 
    return False 



    


@pytest.mark.parametrize(
    "input, substring, expected",
    [
        ("aefoaefcdaefcdaed", "aefcdaed", True),
        ("abcdabcabcabcdf", "abcdf", True),
        ("hello", "hellothere", False),
        ("", "", True)
    ]
)

def test_bruteforce_string_search(input, substring, expected):
    assert bruteforce_string_search(input, substring) == expected

def test_does_not_mutate_input():
    input_string = "abcdef"
    bruteforce_string_search(input_string, "abc")
    assert input_string == "abcdef"

if __name__ == "__main__":
    pytest.main([__file__]) 
