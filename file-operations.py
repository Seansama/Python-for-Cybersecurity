# Read from a file

file = open('assets/myfile.txt', 'r')
data = file.read()
file.close()
print(data)
# Reading from a file using a with statement
with open('assets/myfile.txt', 'r') as f:
    try:
        content = f.read()
    except FileNotFoundError:
        print('Please check if file exists and try again.')
    finally:
        print(content)

# Writing into files

file_a = open('assets/myfile.txt', 'w')
file_a.write(input('Please type some text: '))
file_a.close()

# Writing into file using with statement
with open('assets/myfile.txt', 'w') as f:
    f.write(input('Please type some text: '))
