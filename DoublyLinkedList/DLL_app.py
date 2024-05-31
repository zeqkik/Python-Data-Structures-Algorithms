from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList(1)
dll.append(2)
print('list created with a node value 1 and appended a node with value 2:')
dll.print_list()
print('after pop:')
dll.pop()
dll.print_list()

dll.prepend(2)
print('after prepend:')
dll.print_list()
dll.pop_first()
print('after pop first:')
dll.print_list()

dll.pop_first()
dll.append(1)
dll.append(2)
dll.append(3)

print('getting value in index 1:')
print(dll.get(1).value)

print('setting value in index 1:')
dll.set_value(1, 50)
print(dll.get(1).value)


## Print insert and remove