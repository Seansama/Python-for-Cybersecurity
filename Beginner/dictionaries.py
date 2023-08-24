person = {'name': 'Mark', 'age': '25', 'Gender': 'Male'}
print(person['name'])

# Add a new key/value pair
person['height'] = '6 foot'
print(person)

# Dictionary Methods
# Items
print(person.items())
# Keys
print(person.keys())
# Values
print(person.values())

# Membership operators

x = [1, 2, 3]
print(2 in x)  # True
print(7 in x)  # False
print(1 not in x)  # False
print(5 not in x)  # True

# Is/ is not

y = 10
if type(y) is int:
    print(f'{y} is int')
else:
    print(f'{y} is not int')
