# Dunder (__*__)

class Person:

    def __init__(self, f_name, l_name, age, height):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.height = height

    def __str__(self):
        return f' My name is {self.f_name} {self.l_name}. I am {self.age} and {self.height} centimeters tall.'


p1 = Person('Loraine', 'Hawkins', 25, 181)
# p1.__str__()
print(p1)


class Employee(Person):

    def __init__(self, f_name, l_name, age, height, job, salary):
        super().__init__(f_name, l_name, age, height)
        self.job = job
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12


emp1 = Employee('Mayuki', 'Shizagawa', 46, 172, 'Electrical engineer', 4000)
