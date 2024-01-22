from Stacks.Stack import Stack


class StackQueue:
    stack1 = Stack()
    stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            return

        self.move_stack1_to_stack2()

        return self.stack2.pop()

    def move_stack1_to_stack2(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

    def peek(self):
        if self.is_empty():
            return

        self.move_stack1_to_stack2()

        return self.stack2.peek()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()



