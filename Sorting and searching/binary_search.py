def binary_search(input_array, value):
    middle = len(input_array) // 2
    high_index = len(input_array) - 1
    while True:
        if value == input_array[middle]:
            return middle
        else:
            if middle == high_index:
                break
            elif value > input_array[middle]:
                middle += (middle // 2)
            elif value < input_array[middle]:
                high_index = middle
                middle = high_index // 2
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
