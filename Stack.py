from threading import Lock

from Node import DecoratedNode


class Stack:
    def __init__(self):
        self.Head = None
        self.NodeCount = 0
        self._lock = Lock()

    def push(self, key: int, value: int) -> bool:
        """
         Method to safely push element to stack
         :param key: int, key of element to be pushed into stack
         :param value: value of element to be pushed into stack
         :return: True in case of success, otherwise false
         """
        if not (isinstance(key, int) & isinstance(value, int)):
            return False

        node = DecoratedNode(key, value)
        node.is_head = True

        with self._lock:
            if self.Head is None:
                self.Head = node
            else:
                top = self.Head
                top.is_head = False
                self.Head = node
                self.Head.Next = top

            self.NodeCount += 1
        return True

    def pop(self) -> DecoratedNode:
        """
         Method to safely pop element from stack
         :return: DecoratedNode in case of success, otherwise None
         """
        with self._lock:
            if self.Head is not None and self.NodeCount == 1:
                head = self.Head
                self.Head = None
                self.NodeCount = 0
                return head
            elif self.Head is not None and self.NodeCount > 1:
                head = self.Head
                self.Head = head.Next
                self.Head.is_head = True
                self.NodeCount -= 1
                return head
            else:
                return None

   def __str__(self):
        """
        Method to return string representation of current items in Stack
        :return: string representation of current items in Stack
        """
        descriptions = ''

        with self._lock:
            next_node = self.Head
            while next_node is not None:
                descriptions += next_node.__str__() + ', '
                next_node = next_node.Next
        return descriptions[:-2]