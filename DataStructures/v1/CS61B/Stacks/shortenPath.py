from minmaxstack import simpleAssert

def shortenPath(path : str) -> str:
    stack = []

    if path[0] == "/":
        stack.append("")
    
    tokens = filter(isImportant, path.split("/"))

    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)
    
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)


def isImportant(token: str) -> bool:
    return len(token) > 0 and token != "."



simpleAssert(shortenPath("/foo/../test/../test/../foo//bar/./baz"), "/foo/bar/baz")
simpleAssert(shortenPath("/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../.."), "/")