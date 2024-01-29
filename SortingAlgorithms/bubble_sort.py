def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


numbers = [50, 5, 70, 40, 50, 9]
numbers = bubble_sort(numbers)
print(numbers)
