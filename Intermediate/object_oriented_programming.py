class Person:

    amount = 0  # Class variables. Applies to ALL instances of a class

    def __init__(self, name, age, height):  # Constructor function
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1  # Increase amount counter by one every time an object instance is initialized

    def __del__(self):  # Destructor function
        Person.amount -= 1  # Reduce amount counter by one every time an object instance is deleted
        print('Object deleted')

    def __str__(self):  # Print object as string
        return 'Name: {}, Age: {}, Height: {}'.format(self.name, self.age, self.height)


person1 = Person('Shaun', 19, 175)  # Instance of class Person
print(person1.name, person1.age, person1.height)

person1.name = 'Allen'  # Reassigning an instance attribute
print(person1.name)

# del person1
print(person1)
person2 = Person('Shaun', 21, 185)
print(Person.amount)
