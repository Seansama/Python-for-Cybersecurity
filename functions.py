def my_function(n):
    if n.isdigit():
        print(int(n) * 12)
    else:
        print('Please input a character that is an integer.')


my_function(input('Please put in an integer: '))


# Challenge
def my_full_name(n):
    print('Your name is ' + n + ' Njihia' + ' Mwangi')


my_full_name(input('What is your first name? '))
