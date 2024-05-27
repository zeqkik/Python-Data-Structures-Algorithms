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
print("Question 3 - Pop")
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print("\n")

## Question 4 - Prepend ###
print("Question 4 - Prepend")
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()
print("\n")

## Question 5 - Pop First ###
print("Question 5 - Pop First")
my_linked_list.pop_first()
my_linked_list.print_list()
print("\n")

## Question 6 - Get ###
print("Question 6 - Get")
print(my_linked_list.get(1))
print(my_linked_list.get(2))
print("\n")

## Question 7 - Set Value ###
print("Question 7 - Set")
my_linked_list.set_value(1,20)
my_linked_list.print_list()
print("\n")

## Question 8 - Insert
print("Question 8 - Insert")
my_linked_list.append(3)
print("before insert")
my_linked_list.print_list()
my_linked_list.insert(1,89)
print("after insert 89 on index 1:")
my_linked_list.print_list()
print("\n")

## Question 9 - Remove
print("Question 9 - Remove")
print("before remove")
my_linked_list.print_list()
print("after remove index 1:")
my_linked_list.remove(1)
my_linked_list.print_list()
print("\n")

## Question 10 - Reverse
print("Question 9 - Reverse")
print("before reverse")
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print("after reverse")
my_linked_list.reverse()
my_linked_list.print_list()
print("\n")
