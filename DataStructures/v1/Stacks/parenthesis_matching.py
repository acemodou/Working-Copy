from stack_adt_linkedlist import STACKLIST

def simple_assert(a, b):
    assert a == b, f'{a} != {b}'

def is_balance(exp):
    '''There are two cases for inbalance
    1. We finish iterating and there is something left in the stack
    2. We didn't finish and there is nothing to pop'''

    stack = STACKLIST()
    for barackets in exp:
        if barackets == "(":
            stack.push(barackets)
        elif barackets == ")":
            if stack.isEmpty():
                return False 
            stack.pop()
    return stack.isEmpty() 

simple_assert(is_balance("(a+b)*(c-d)"),True)
simple_assert(is_balance("((a+b)*(c-d)"),False)
simple_assert(is_balance("((a+b)*(c-d)))"),False)