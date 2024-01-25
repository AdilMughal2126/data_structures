from LinkedList.LinkedList import LinkedList


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self, size):
        self.items = [None] * size
        self.size = size

    def hash(self, key):
        return key % len(self.items)

    def put(self, key, value):
        entry = self.get_entry(key)

        if entry is not None:
            entry.value = value
            return

        self.get_or_create_bucket(key).add_last(KeyValuePair(key, value))

    def get(self, key):
        entry = self.get_entry(key)
        if entry is None:
            return entry.value
        return entry

    def get_entry(self, key):
        bucket = self.get_bucket(key)

        while bucket is not None:
            key_value_pair = bucket.value
            bucket = bucket.next
            if key_value_pair.key == key:
                return key_value_pair

        return None

    def get_or_create_bucket(self, key):
        index = self.hash(key)
        bucket = self.items[index]

        if bucket is None:
            bucket = LinkedList()
            self.items[index] = bucket

        return bucket

    def get_bucket(self, key):
        bucket = self.items[self.hash(key)]

        if bucket is None:
            return None

        return bucket.first
