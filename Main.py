from threading import Thread

from Node import DecoratedNode

from LinkedList import LinkedList, SafeLinkedList
from Hashtable import UnsafeHashTable, FastSafeHashTable, SafeHashTable
from Stack import Stack, SafeStack

stack = SafeStack()

def PushItemsToStack(stack : SafeStack):
    i = 0
    for arf in range(10):
    #while True:
        i += 1
        stack.push(i, i)
        print("Stack pushed: ", stack.__str__())

def PopStack(stack : SafeStack):
    while stack.NodeCount > 0:
        stack.pop()
        print("Stack poped: ", stack.__str__())


if __name__ == "__main__":


    t1 = Thread(target=PushItemsToStack, args = (stack, ))
    t2 = Thread(target=PopStack, args = (stack, ))

    t1.start()
    t2.start()