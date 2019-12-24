import sys

def get_hour_glass_text_Int(file_path):
    """
    open a file, read as list and split to remove new line
    loop through the list, and assign it to a new list whilst splitting
    loop through the second list and cast to ints
    store the new list in the outler list
    :param file_path:
    :return: outler list
    """

    with open(file_path, 'r') as f:
        file_contents = f.read().split('\n')
        output_list = list()

        for values in file_contents:
            store_new_values = values.split()
            inner_list = []
            for num in store_new_values:
                inner_list.append(int(num))
            output_list.append(inner_list)
    return output_list

def _hourglass(arr):
    




if __name__ =="__main__":
    text_file = get_hour_glass_text_Int('hourglass.txt')
    print(text_file)


    # hour_glass = [[1, 1, 1, 0, 0, 0],
    #               [0, 1, 0, 0, 0, 0],
    #               [1, 1, 1, 0, 0, 0],
    #               [0, 0, 2, 4, 4, 0],
    #               [0, 0, 0, 2, 0, 0],
    #               [0, 0, 1, 2, 4, 0]]

    # _hourglass(hour_glass)

