def binary_search(input_array, value, min = 0, max = None):
    if max is None:
        max = len(input_array)

    mid = (min + max) / 2
    if mid == len(input_array):
        return False
    elif input_array[mid] == value:
        return mid
    elif max == min:
        return False
    elif input_array[mid] < value:
        return binary_search(input_array, value, mid + 1, max)
    else:
        return binary_search(input_array, value, min, mid)
