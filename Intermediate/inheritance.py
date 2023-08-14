class Person:
    amount = 0  # Class variables. Applies to ALL instances of a class

    def __init__(self, name, age, height):  # Constructor function
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1  # Increase amount counter by one every time an object instance is initialized

    # def __del__(self):  # Destructor function
    #     Person.amount -= 1  # Reduce amount counter by one every time an object instance is deleted
    #     print('Object deleted')

    def __str__(self):  # Print object as string
        return 'Name: {}, Age: {}, Height: {}'.format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):  # Overriding a Class function
        text = super(Worker, self).__str__()
        text += ', Salary: {}'.format(str(self.salary))
        return text

    def calculate_yearly_salary(self):
        return self.salary * 12


worker1 = Worker('Henry', 32, 186, 4000)
print(worker1)
print(worker1.calculate_yearly_salary())
