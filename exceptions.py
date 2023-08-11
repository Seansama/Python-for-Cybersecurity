# Handling Exceptions
try:
    x = int(input('First number: '))
    y = int(input('Second number: '))
    print(x / y)
except ValueError:
    print('Please enter a valid number.')
    y = int(input('First number: '))
    x = int(input('Second number: '))
    print(x / y)
except ZeroDivisionError:
    print('Cannot divide by zero. Please ensure a zero is not provided as a number.')
    y = int(input('First number: '))
    x = int(input('Second number: '))
    print(x / y)
finally:
    print('Function complete!')


# Raising exceptions
def division(a, b):
    if a and b != 0 and a and b == int:
        print(a / b)
    elif a or b == 0:
        raise ZeroDivisionError('Cannot divide by zero. Please try again.')
    elif a or b is not int:
        raise ValueError('Please enter a valid number.')


division(int(input('Please enter first number: ')), int(input('Please enter second number: ')))

# Assertions
k = 100
y = 20

assert (x < y)
