from threading import Lock

from LinkedList import SafeLinkedList, LinkedList
from Node import DecoratedNode


class FastHashtable:
    def __init__(self):
        self.first_bucket = SafeLinkedList()
        self.second_bucket = SafeLinkedList()
        self.third_bucket = SafeLinkedList()
        self.NodeCount = 0

    def add(self, key: int, value: int) -> bool:
        """
         Method to safely add element to Hashtable
         :param key: int, key of element to be added into Hashtable
         :param value: value of element to be added into Hashtable
         :return: True in case of success, otherwise false
         """

        if not (isinstance(key, int) & isinstance(value, int)):
            return False

        node = DecoratedNode(key, value)
        bucket_num = node.key % 3

        if bucket_num == 0:
            self.first_bucket.add_node(node)
        elif bucket_num == 1:
            self.second_bucket.add_node(node)
        elif bucket_num == 2:
            self.third_bucket.add_node(node)
        else:
            raise ValueError("[ ERROR ] Adding Node to the HashTable failed - impossible index: " + str(bucket_num))

        return True

    @property
    def node_count(self) -> int:
        return self.first_bucket.NodeCount + self.second_bucket.NodeCount + self.third_bucket.NodeCount;

    def get(self, key: int) -> int:
        """
         Method to safely add element to Hashtable
         :param key: int, key of element to be added into Hashtable
         :return: int value in case of success, otherwise raise the exception
         """
        if not (isinstance(key, int)):
            raise ValueError("[ ERROR ] Key of Hashtable has a wrong type: " + str(key))

        bucket_num = key % 3

        if bucket_num == 0:
            return self.first_bucket.find_node(key).value
        elif bucket_num == 1:
            return self.second_bucket.find_node(key).value
        elif bucket_num == 2:
            return self.third_bucket.find_node(key).value
        else:
            raise ValueError("[ ERROR ] Unable to find node in Hashtable - impossible index: " + str(key))
