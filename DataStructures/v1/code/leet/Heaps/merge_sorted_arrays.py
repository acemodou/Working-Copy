def mergeSortedArrays(arrays):
    current_positions = [0 for _ in arrays]
    sorted_list = []
    while True:
        smallest_list_of_elements = []
        for idx in range(len(arrays)):
            sub_arrays = arrays[idx]
            element_idx = current_positions[idx]
            if element_idx == len(sub_arrays):
                continue
            smallest_list_of_elements.append({"array_idx" : idx, "value" : sub_arrays[element_idx]})
        if len(smallest_list_of_elements) == 0:
            break
        min_value = get_minimum(smallest_list_of_elements)
        current_positions[min_value["array_idx"]] +=1
        sorted_list.append(min_value["value"])
    return sorted_list
        
def get_minimum(items):
    min_value_idx = 0
    for idx in range(1, len(items)):
        if items[idx]["value"] < items[min_value_idx]["value"]:
            min_value_idx = idx 
    return items[min_value_idx]
