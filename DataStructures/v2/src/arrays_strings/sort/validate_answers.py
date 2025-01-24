def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


def validate_answers(func):
    input = [8, 5, 7, 3, 2]
    expected = [2, 3, 5, 7, 8]
    actual = func(input)
    simple_assert(actual, expected)