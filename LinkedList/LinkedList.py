class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add_first(self, item):
        node = Node(item)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

    def add_last(self, item):
        node = Node(item)

        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def delete_first(self):
        if self.first == self.last:
            self.first = None
            self.last = None

        if self.first is not None:
            self.first = self.first.next

    def delete_last(self):
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            while temp.next != self.last:
                temp = temp.next

            temp.next = None
            self.last = temp

    def contains(self, item):
        temp = self.first
        while temp is not None:
            if temp.value == item:
                return True
            temp = temp.next
        return False

    def index_of(self, item):
        temp = self.first
        count = 0

        while temp is not None:
            if temp.value == item:
                return count

            temp = temp.next
            count += 1
        return -1

    def reverse(self):
        current = self.first
        prev = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.last = self.first
        self.first = prev














    def print_list(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
