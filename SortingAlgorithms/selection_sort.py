def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


numbers = [90, 8, 28, 7]
print(selection_sort(numbers))
