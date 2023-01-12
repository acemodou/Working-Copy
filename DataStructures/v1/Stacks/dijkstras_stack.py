from stack_adt_using_arrays import STACK
def simple_assert(a,b):
    assert a == b, f'{a}!{b}'

def evaluate(tokens):
    value = STACK(6)
    value.initialize()
    operator = STACK(6)
    operator.initialize()
    token = 0
    while token < len(tokens):
        if tokens[token] == " " or tokens[token] == "(":
            token +=1
            continue
        elif tokens[token] == "+":
            operator.Push(tokens[token])
            token +=1
        elif tokens[token] == "-":
            operator.Push(tokens[token])
            token +=1
        elif tokens[token] == "*":
            operator.Push(tokens[token])
            token +=1
        elif tokens[token] == "/":
            operator.Push(tokens[token])
            token +=1
        elif tokens[token] == "sqrt":
            operator.Push(tokens[token])
            token +=1
        elif tokens[token] == ")":
            val = value.Pop()
            op = operator.Pop()
            if op == "+": result = val + value.Pop()
            elif op == "-": result = val - value.Pop()
            elif op == "*": result = val * value.Pop()
            elif op == "/": result = val / value.Pop()
            value.Push(int(result))
            token +=1
        else:
            result = 0
            while token < len(tokens) and tokens[token].isdigit() and tokens[token] != " ":
                result = result * 10 + int(tokens[token])
                token +=1
            value.Push(result)
    return value.Pop()

simple_assert(evaluate("(10 + (2 * 6))"), 22)
simple_assert(evaluate("(100 * 2) + 12)"),212)
