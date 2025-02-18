from threading import Lock

from LinkedList import LinkedList, SafeLinkedList
from Node import DecoratedNode


class UnsafeHashTable:
    def __init__(self):
        self.first_bucket = LinkedList()
        self.second_bucket = LinkedList()
        self.third_bucket = LinkedList()
        self.Sum = 0
        self.NodeCount = 0

    def add(self, key, value):
        node = DecoratedNode(key, value)

        bucket_number = node.key % 3
        if bucket_number == 1:
            self.first_bucket.add_node(node)
            self.NodeCount += 1
            return
        if bucket_number == 2:
            self.NodeCount += 1
            self.second_bucket.add_node(node)
            return
        if bucket_number == 0:
            self.NodeCount += 1
            self.third_bucket.add_node(node)
            return
        raise ValueError("[ ERROR ] Adding Node to the HashTable failed - impossible index: " + str(bucket_number))

    def get(self, key: int):
        bucket_number = key % 3
        if bucket_number == 1:
            result = self.first_bucket.find_node(key)
            return result
        if bucket_number == 2:
            result = self.second_bucket.find_node(key)
            return result
        if bucket_number == 0:
            result = self.third_bucket.find_node(key)
            return result


class SafeHashTable(UnsafeHashTable):
    # TODO: This class is  bad for writing.
    #  Why is it so, where is the bottleneck? Can we improve it?
    def __init__(self):
        super().__init__()
        self.lock = Lock()


class FastSafeHashTable(SafeHashTable):
    def __init__(self):
        super().__init__()
        self.first_bucket = SafeLinkedList()
        self.second_bucket = SafeLinkedList()
        self.third_bucket = SafeLinkedList()
