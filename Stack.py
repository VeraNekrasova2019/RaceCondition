from threading import Lock

from Node import DecoratedNode

class Stack:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.NodeCount = 0
        self.Sum = 0

    def push(self, key : int, value : int):
        node = DecoratedNode(key, value) 
        node.is_head = True

        if self.Head is None:
           self.Head = self.Tail = node
        else:
            top = self.Head
            top.is_head = False
            self.Head = node
            self.Head.Next = top
       
        self.NodeCount += 1
     
    def pop (self) -> DecoratedNode:
        if self.Head is not None and self.NodeCount == 1:
            head = self.Head
            self.Head = self.Tail = None
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

    def push(self, key : int, value : int):
        with self.lock:
            super().push(key, value)
        return self.NodeCount

    def pop (self) -> DecoratedNode:
        with self.lock:
            node = super().pop()
        return node
    
    def __str__(self):
        with self.lock:
            str = super().__str__()
        return str