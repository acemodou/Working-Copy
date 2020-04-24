import searching_arrays
import arrayRotation


def findArrayRotation(arr, n):
    print(F"-I- Kicking off array rotation {arr}")
    print(F"-I- Calling the juggling algorithm")

    rotated_arr = arrayRotation.juggling_algorithm(arr, n, d=4)
    print(F"-I- Finding the minimum element in a rotated array {rotated_arr} ")
    find_piv = searching_arrays.find_pivot(arr, n, 0, n - 1)
    return find_piv


if __name__ == "__main__":

    arr = [5, 6, 8, 10, 12, 15, 22, 23, 28, 31, 38]
    print(F"Array is rotated and the pivot is : {findArrayRotation(arr,11)} respectively")




