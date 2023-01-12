from stack_adt_linkedlist import STACKLIST

def simple_assert(a, b):
    assert a == b, f'{a} != {b}'


def infix_to_postfix(exp):
    stack = STACKLIST()
    stack.push("#")
    post_fix = []
    """ We need to check if its and operand, we need to check precedence 
    we push to our stack when the precedence is higher 
    if we get to the end and the stack is not empty we pop everything to post fix then return postfix
    """
    i= 0
    while i < len(exp):
        if is_operand(exp[i]):
            post_fix.append(exp[i])
            i +=1
        else:
            if precedence(exp[i]) > precedence(stack.stackTop()):
                stack.push(exp[i])
                i +=1
            else:
                x = stack.pop()
                post_fix.append(x) 
    while not stack.isEmpty():
        x = stack.pop()
        post_fix.append(x)
    post_fix ="".join(post_fix[:len(post_fix)-1:])
    return post_fix 

def is_operand(value):
    if value == "+" or value == "-" or value == "*" or value == "/":
        return 0
    else:
        return 1 

def precedence(value):
    if value == "+" or  value == "-":
        return 1
    elif value == "*" or  value == "/":
        return 2
    else:
        return 0

simple_assert(infix_to_postfix("a+b*c"),"abc*+" )