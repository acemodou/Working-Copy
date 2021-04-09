
def biggest(i, j):
    if i > j:
        return  i 
    else:
        return j

def largestCat(cats):
    '''
    Display the largest cat within it's 4 neighbors
    '''
    counter = 0
    max_cat = 0
    previous_largest = 0
    for i in range(len(cats)):
        j = 0
        while j <=i+4 and j < len(cats):
            res = biggest(cats[i], cats[j])
            if res > max_cat:
                max_cat = res
            counter +=1
            j +=1
        if max_cat !=previous_largest:
            print(max_cat)
        i = counter
        previous_largest = max_cat


cats = [10]
largestCat(cats)

