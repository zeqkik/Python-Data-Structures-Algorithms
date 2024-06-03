from ..LinkedLists.Node import Node

class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.value = value
        self.next = None
