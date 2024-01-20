from Queues.ArrayQueue import ArrayQueue

array_queue = ArrayQueue(5)
array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)
array_queue.enqueue(4)
array_queue.enqueue(5)

print(array_queue.dequeue())
print(array_queue.dequeue())

