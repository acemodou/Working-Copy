

def even_odd_Str():
    """
     Given a string,
     of length  that is indexed from  to N-1 , print its even-indexed and odd-indexed characters
      as  space-separated strings on a single line (see the Sample below for more detail).
     Input :
     2
    Hacker
    Rank

    Output:
    Hce akr
    Rn ak
    :return:
    """

    for i in range(int(input())): # Tells you how many time we want to enter input
        s = input() # will go depending on the loop
        print(s[::2], s[1::2])



def reverse_array(a):

    # for i in arr[::-1]:
    #     print(i, end=" ")
    # a = [i for i in arr[::-1]]
    # print(a)
    b = a.reverse()
    print(b)
if __name__=="__main__":
    print("Enter how many string you want to input ")
    arr = [1,2,3,4]
    #even_odd_Str()
    reverse_array(arr)