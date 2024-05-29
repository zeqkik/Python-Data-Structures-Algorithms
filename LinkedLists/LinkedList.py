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
            return temp.value
        else:
            temp = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -=1
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:    
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): #_ can be used if we don't use the iterate variable
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if(self.head == self.tail):
            return self.head
        step = 0
        faster = self.head
        slow = self.head
        while faster.next is not None:
            faster = faster.next
            step += 1
            if(step % 2 == 0):
                slow = slow.next
        if(step % 2 != 0):
            return slow.next
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        step = 0
        while(fast is not None):
            fast = fast.next
            step += 1
            if (step % 2 == 0):
                slow = slow.next
            if(fast == slow):
                return True
        return False    