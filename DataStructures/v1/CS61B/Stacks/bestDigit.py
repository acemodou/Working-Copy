def bestDigits(number, numDigits):
    # Write your code here.
    stackWithBestDigits = []
    for num in number:
        while numDigits > 0 and len(stackWithBestDigits) and num > stackWithBestDigits[-1]:
            stackWithBestDigits.pop()
            numDigits -= 1
        stackWithBestDigits.append(num)
    while numDigits > 0:
        stackWithBestDigits.pop()
        numDigits -= 1
    return "".join(stackWithBestDigits)
