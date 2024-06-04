from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print(bst.contains(1))
print(bst.contains(2))
print(bst.contains(3))
print(bst.contains(4))