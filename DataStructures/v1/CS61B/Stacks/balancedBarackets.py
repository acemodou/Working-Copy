def balancedBrackets(string):
    stack = []
    openParens = "({["
    closeParens = ")}]"
    matchingBarackets = {")":"(", "]":"[", "}":"{"}
    for parens in string:
        if parens in openParens:
            stack.append(parens)
        elif parens in closeParens:
            if not stack:
                return False 
            if stack[-1] == matchingBarackets[parens]:
                stack.pop()
            else:
                return False 
        
    return len(stack) == 0
        
