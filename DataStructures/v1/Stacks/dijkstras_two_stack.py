import math
def simple_assert(a,b):
    assert a == b, f'{a}!{b}'

def evaluate(tokens):
    operators = []
    values = []
    # Read token, push if operator
    i = 0
    while i < len(tokens):
        if tokens[i] == ' ' or tokens[i] == "(":
            i += 1
            continue
        elif tokens[i] == '+':
            operators.append(tokens[i])
            i += 1
        elif tokens[i] == '-':
            operators.append(tokens[i])
            i += 1
        elif tokens[i] == '*':
            operators.append(tokens[i])
            i += 1
        elif tokens[i] == '/':
            operators.append(tokens[i])
            i += 1
        elif tokens[i] == 'sqrt':
            operators.append(tokens[i])
            i += 1
        elif tokens[i] == ")":
            # pop, evaluate and push result if token is ")"
            op = operators.pop()
            val = values.pop()
            if op == "+": val = values.pop() + val
            elif op == "-": val = values.pop() - val
            elif op == "*":val = values.pop() * val
            elif op == "/": val = values.pop() / val
            elif op == "sqrt": val = math.sqrt(val)
            values.append(int(val))
            i += 1
        else:   
            # Get digits from the strings
            val = 0
            while i < len(tokens) and tokens[i].isdigit() and tokens[i] != ' ':
                val = (val * 10) + int(tokens[i])
                i += 1

            values.append(val)
    return values.pop()

simple_assert(evaluate("(10 + (2 * 6))"), 22)
simple_assert(evaluate("(100 * 2) + 12)"),212)
