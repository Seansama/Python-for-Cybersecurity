# Print the length of a string
#  is an array/list of characters
text = 'Hello world'
print(len(text))

# Slicing a string
a = 'Hi There!'
print(a[3:])  # There!
print(a[:3])  # Hi

# iterate over a string
for i in text:
    print(i)

# Escape characters
# Line break
b = 'Hello world! \nThis day is awesome!!'
print(b)

# String formatting
name = input('What is your name? ')
age = int(input('What is your age? '))
print('My name is %s and I am %d years old!' % (name, age))
print('My name is {} and I am {} years old.'.format(name, age))

# String functions
# Case manipulation function
c = 'This is my text!'
print(c.upper())
print(c.lower())
print(c.title())
print(c.swapcase())
print(c.capitalize())

#  Count functions
d = 'I am Shaun and I am happy because I enjoy programming!'
print(d.count('I'))  # Count how many times a substring occurs in a string

# Find function
print(d.find('enjoy'))  # find what index a string or substring occurs at

# Join function
separator = '; '
mylist = ['Car', 'Zesty', 'Money']
print(separator.join(mylist))  # Joins elements of a list/string separated by a predefined separator

# Split function
write = 'I am happy because I have a fwb.'
words = write.split(' ')  # Split words in a string into elements in a list
print(words)

# Replace function
x = 'My name is Shaun'
print(x)
print(x.replace('Shaun', 'Allen'))  # Replace a character/substring in a string or an element in a list
