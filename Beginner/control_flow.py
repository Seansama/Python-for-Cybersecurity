# var = int(input('What is your age? '))
#
# if var <= 5:
#     print('You are a kid.')
# elif var <= 15:
#     print('You are a big kid.')
# elif var <= 21:
#     print('You are a teenager.')
# else:
#     print('You are grown now. An adult!')


# Challenge

temp = int(input('Please input the current temperature '))

if temp <= 20:
    print('You need boots!')
elif temp <= 30:
    print('You need a coat!')
elif temp <= 70:
    print('You need a jacket!')
elif 70 < temp <= 100:
    print('It is nice outside!')
else:
    print('It is scorching!')
