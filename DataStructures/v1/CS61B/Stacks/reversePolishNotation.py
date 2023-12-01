from minmaxstack import simpleAssert
from typing import Union

def reversePolishNotation(tokens : str) -> Union[int, float]:
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            lastNum = stack.pop()
            stack.append(stack.pop() - lastNum)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            lastNum = stack.pop()
            stack.append(int(stack.pop() / lastNum))
        else:
            stack.append(int(token))
    return stack.pop()
          


simpleAssert(reversePolishNotation(["10"]), 10)
simpleAssert(reversePolishNotation(["10", "5", "-"]), 5)
simpleAssert(reversePolishNotation(["10", "5", "*"]), 50)
