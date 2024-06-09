from HashTable import HashTable

hash = HashTable()


hash.set_item('bolts', 1400)
hash.set_item('washers', 50)
hash.set_item('lumber', 70)

print(hash.get_item('bolts'))
print(hash.get_item('washers'))
print(hash.get_item('lumber'))

print(hash.keys())