# Sorting lists, tuples, and objects in Python

# List sorting
li = [5, 2, 9, 1, 5, 6]
s_li = sorted(li)  # Returns a new sorted list
s_li = sorted(li, reverse=True)  # Sorts in descending order
print('Reversed sorted Variable:\t', s_li)  # [9, 6, 5, 5, 2, 1]

print('sorted Variable:\t', s_li)  # [1, 2, 5, 5, 6, 9]

li.sort()  # Sorts the list in place

print('Original List:\t', li)  # [5, 2, 9, 1, 5, 6]

# Tuple sorting
tu = (3, 6, 1, 8, 2)
s_tup = sorted(tu)  # Returns a new sorted list
print('Tuple\t', s_tup)  # [1, 2, 3, 6, 8]

# Dictionary sorting by keys
di = {'name': 'John', 'age': 25, 'city': 'New York'}
s_di = sorted(di)  # Sorts the keys of the dictionary




