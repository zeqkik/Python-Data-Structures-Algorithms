from Node import Node

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #last node point to the new node
            self.tail = new_node
        self.length+=1
        return True 
    
    def pop(self):
        if(self.length == 0):
            return None
        elif(self.length == 1):
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -=1
            return temp
        else:
            temp = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -=1
        return temp