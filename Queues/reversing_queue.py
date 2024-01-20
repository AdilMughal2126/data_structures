from queue import Queue

numbers = Queue()
numbers.put(1)
numbers.put(2)
numbers.put(3)


def reverse_queue(queue):
    numbers_stack = []
    while not queue.empty():
        number = queue.get()
        numbers_stack.append(number)
    for number in numbers_stack:
        item = numbers_stack.pop()
        queue.put(item)


reverse_queue(numbers)

print(numbers.get())


