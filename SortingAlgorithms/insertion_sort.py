def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        unsorted_element = array[i]
        j = i
        while j > 0 and array[j - 1] > unsorted_element:
            array[j] = array[j - 1]
            j -= 1
        array[j] = unsorted_element

    return array


numbers = insertion_sort([50, 40, 30, 20, 10])
print(numbers)

