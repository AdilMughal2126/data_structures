class ArrayQueue:
    front = rear = 0
    items = []
    count = 0

    def __init__(self, size):
        self.size = size
        self.items = [None] * size

    def enqueue(self, item):
        if self.count == self.size:
            print("Queue is full.")
            return

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.size  # Fix here
        self.count += 1

    def dequeue(self):
        item = self.items[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def is_full(self):
        return self.count == self.size


