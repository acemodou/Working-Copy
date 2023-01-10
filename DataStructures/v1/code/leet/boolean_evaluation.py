import collections 

def characterToBoolean(s):
    return True if s == '1' else False

def boolToString(boolValue):
    return '#True' if boolValue else '#False'

def countEvals(s, result, memo):
    if not len(s):
        return 0
        
    if len(s) == 1:
        return 1 if result == characterToBoolean(s) else 0 
    
    if memo[s + boolToString(result)]:
        return memo[s + boolToString(result)]
    
    ways = 0
    # Split left and right substring with boolean operator 
    for idx in range(1, len(s), 2):
        booleanOperator = s[idx]
        left = s[:idx]
        right = s[idx+1:]
        
        # Evaluate left and right substring for false and true 
        leftTrue = countEvals(left, True, memo)
        leftFalse = countEvals(left, False, memo)
        rightTrue = countEvals(right, True, memo)
        rightFalse = countEvals(right, False, memo)
        
        total = (leftTrue * leftFalse) + (rightTrue * rightFalse)
    
        # Calculate number of ways we can have true if boolean operator between left
        # and right substring is XOR, AND and OR.
        # For XOR both left and right substring should evaluate to different.
        # For AND both left and right substring should evaluate to True.
        # For OR either left or right should evaluate to True.
        
        if booleanOperator == '^':
            totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue)
        elif booleanOperator == '&':
            totalTrue = leftTrue * rightTrue
        elif booleanOperator == '|':
            totalTrue = (leftTrue * rightFalse + leftFalse * rightTrue + leftTrue * rightTrue)
        
        else:
            totalTrue = 0
            print(f'Invalid operator: {booleanOperator}')
        
        subWays = totalTrue if result else total - totalTrue
        ways += subWays 
        memo[s + boolToString(result)] = ways
        return ways 
            
def main():
    memo = collections.defaultdict(int)
    # s = input('Enter boolean expression: ')
    s = '1^0'
    result = int(input('Enter expected result(0, 1): '))
    result = bool(result)
    print('Number of ways: {ways}'.format(ways=countEvals(s, result, memo)))

    
if __name__ =="__main__":
    main()