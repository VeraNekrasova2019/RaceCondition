from threading import Lock
import logging

from Node import DecoratedNode


class Stack:

    def __init__(self):
        self.Head = None
        self.NodeCount = 0
        self.Sum = 0

    def push(self, key: int, value: int) -> bool:
        """
        Method to push element to stack
        :param key: int, key of element to be pushed into stack
        :param value: value of element to be pushed into stack
        :return: True in case of success, otherwise false
        """
        try:
            if not(isinstance(key, int) & isinstance(value, int)):
                return False

            node = DecoratedNode(key, value)
            node.is_head = True

            if self.Head is None:
                self.Head = node
            else:
                top = self.Head
                top.is_head = False
                self.Head = node
                self.Head.Next = top

            self.NodeCount += 1
            return True
        except Exception:
            return False

    def pop(self) -> DecoratedNode:
        """
        Method to pop element from stack
        :return: DecoratedNode in case of success, otherwise None
        """
        try:
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
        except Exception:
            return False

    def __str__(self):
        """
        Method to return string representation of current items in Stack
        :return: string representation of current items in Stack
        """
        next_node = self.Head
        descriptions = ''
        while next_node is not None:
            descriptions += next_node.__str__() + ', '
            next_node = next_node.Next
        return descriptions[:-2]


class SafeStack(Stack):
    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def push(self, key: int, value: int) -> bool:
        """
        Safe method to push element to stack
        :param key: int, key of element to be pushed into stack
        :param value: value of element to be pushed into stack
        :return: True in case of success, otherwise false
        """
        with self.lock:
            if not (isinstance(key, int) & isinstance(value, int)):
                return False

            node = DecoratedNode(key, value)
            node.is_head = True

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
        Safe method to pop element from stack
        :return: DecoratedNode in case of success, otherwise None
        """
        with self.lock:
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
        Safe method to return string representation of current items in Stack
        :return: string representation of current items in Stack
        """
        with self.lock:
            next_node = self.Head
            descriptions = ''
            while next_node is not None:
                descriptions += next_node.__str__() + ', '
                next_node = next_node.Next
            return descriptions[:-2]