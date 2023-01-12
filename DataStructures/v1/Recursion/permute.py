def diffDepartNums(policeDept, fireDept, sanitizeDept):
    'Department numbers should be all different'

    return policeDept != fireDept and \
           fireDept != sanitizeDept and \
           policeDept != sanitizeDept


def sumofDepartNumbers(police, fireDept, sanitizeDept):
    'sum of all numbers should be equals to 12'
    return police + fireDept + sanitizeDept == 12


def policeNumIsEven(police):
    'Police number must be even'
    return police % 2 == 0


def validateDepartmentNumbers(policeDept, fireDept, sanitizeDept):
    'Check to make sure all numbers meet theirrequirements'
    return diffDepartNums(policeDept, fireDept, sanitizeDept) and \
           sumofDepartNumbers(policeDept, fireDept, sanitizeDept) and \
            policeNumIsEven(policeDept)
  

def display_valid_dept_permutation(n):
    """
    Permute department numbers from 1 - 7
    Police#, sanitize#, fire# should be all different
    Police# should be even
    sum of police# + sanitize# + fire# should be equals to 12
    """
   
    half_list = n // 2
    terminator = n
    print(F"half of the list is: {half_list}")
    for policeDept in range(1, n + 1):
        # Used terminator to print only half the list
        if terminator == half_list:
            return 
        terminator -=1
        for fireDept in range(1, n + 1):
            for sanitizeDept in range(1, n + 1):
                if validateDepartmentNumbers(policeDept, fireDept, sanitizeDept):
                    print(F'policeDept#: {policeDept} fireDept#: {fireDept} sanitizeDept#: {sanitizeDept}')
                    # Print in reverse to avoid going through the entire list.
                    print(F'sanitizeDept#: {sanitizeDept} fireDept#: {fireDept} policeDept#: {policeDept}')
            
if __name__ =="__main__":
    display_valid_dept_permutation(7)