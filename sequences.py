myList = [10, 20, 30, 'string', True, 8.97]

print(myList[3])
# Slice of 3 values from index 0
print(myList[:3])
# Slice of 2 values starting from the current index to the end of the array
print(myList[1:])

# Reassigning a value to an index in an array
myList[2] = 'Thirty'
print(myList)

# For loops and arrays
numbers = [12, 36, 44, 59, 36]
for i in numbers:
    var = i * 3
    print(f'{i} * 3 is {var}')

# Append two lists
x = [1, 2, 3]
y = [4, 5, 6]

print(x + y)

# Multiply lists by scalars
k = [1, 2, 3, 4, 5]
print(k * 5)

# Functions of lists
# len (length of a list)
print(len(k))
# max (Largest value in a list)
print(max(k))
# min (smallest value in the list)
print(min(k))

# Append (add a value to the end of a list)
k.append('New value')
print(k)

# insert (Add value to any point of array based on index
k.insert(0, 0)
print(k)

# Remove the value in an array(must exist in the list)
k.remove('New value')
print(k)

# Remove element at specific index
k.pop(0)
print(k)

# Find the index of a value
print(k.index(4))

# Sort a list
n = [23, 56, 44, 30, 25, 69, 103, 96]
n.sort()
print(n)

# Tuples(Immutable lists)
# Read operations can be done but not write operations
a = {1, 2, 3}

# Can be type cast though
a = list(a)
a.insert(0, 0)
a = tuple(a)
print(a)
