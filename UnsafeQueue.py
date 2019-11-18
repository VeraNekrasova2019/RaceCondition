from threading import Lock

from Node import DecoratedNode, QueueDecoratedNode

class UnsafeQueue:

    def __init__(self):
        self.Head = None
        self.Tail = None
        self.NodeCount = 0
        self.Sum = 0

    def enqueue(self, key : int, value : int):
        
        node = QueueDecoratedNode(key, value) 
        node.is_head = True

        if self.Head is None:
           self.Head = self.Tail = node
        else:
            top = self.Head
            top.is_head = False
            self.Head = node
            self.Head.Next = top
            top.Previous = self.Head
       
        self.NodeCount += 1

    def dequeue(self) -> QueueDecoratedNode:
        tail = self.Tail
        if tail is not None and self.NodeCount == 1:
            self.Head = self.Tail = None
            self.NodeCount = 0
            return tail
        elif tail is not None and self.NodeCount > 1:
            self.Tail = tail.Previous
            self.Tail.Next = None
            self.NodeCount -= 1
            return tail          
        else:
            return None
       
    def __str__(self):
        next_node = self.Head
        descriptions = ''
        while next_node is not None:
            descriptions += next_node.__str__() + ', '
            next_node = next_node.Next
        return descriptions[:-2]

class SafeQueue(UnsafeQueue):
    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def push(self, key : int, value : int):
        with self.lock:
            super().enqueue(key, value)
        return self.NodeCount

    def pop (self) -> QueueDecoratedNode:
        with self.lock:
            node = super().dequeue
        return node
    
    def __str__(self):
        with self.lock:
            str = super().__str__()
        return str