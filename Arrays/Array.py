class Array:
    numbers = []
    count = 0

    def __init__(self, length):
        self.length = length
        self.numbers = [None] * length

    def insert(self, item):
        if self.count < self.length:
            self.numbers[self.count] = item
            self.count += 1
        else:
            self.length = self.length * 2
            tem_array = [None] * self.length

            for i, number in enumerate(self.numbers):
                tem_array[i] = number

            tem_array[self.count] = item
            self.numbers = tem_array
            self.count += 1

    def remove_at(self, index):
        if index < 0 or index > self.count:
            return "invalid index"

        for i in range(self.count):
            if i == index:
                self.numbers[i] = None

        for i in range(index, self.count):
            self.numbers[i] = self.numbers[i + 1]

        self.count -= 1

    def index_of(self, index):
        for i, number in enumerate(self.numbers):
            if number == index:
                return i

        return -1

    def print(self):
        for index in range(self.count):
            print(self.numbers[index], end=" ")
