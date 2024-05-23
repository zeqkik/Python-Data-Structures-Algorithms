##

from LinkedList import LinkedList

###### Question 1 - Constructor ######

my_linked_list = LinkedList(4)
print("Question 1 - Constructor")
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
print("\n")

###### Question 2 - Append ######
print("Question 2 - Constructor")
my_linked_list.append(2)
my_linked_list.print_list()
print("\n")

### Question 3 - Pop ###
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print("\n")
