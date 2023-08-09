# For loop
string = 'Hello World!'
for i in string:
    print(i)

cars = ['Ferrari', 'Mercedes', 'Aston Martin', 'Bugatti', 'Toyota', 'Honda']
for j in cars:
    print(j)

arr = [['one', 'two', 'three'], ['Lewis', 'Max', 'Lando']]
print(arr[0][2], arr[1][0])

# While loop
on = True
i = 0
while on:
    var = input('Continue running loop Y/N ')
    i += 1
    print(i)
    if var == 'N':
        on = False
