import sys
from linkedlist import *

class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert(new_element, 1)

    def pop(self):
        return self.ll.delete(1)
