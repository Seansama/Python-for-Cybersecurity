import threading


def function1():
    for i in range(100):
        print('A')


def function2():
    for i in range(100):
        print('B')


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.start()
t2.start()

# Waiting for threads

t2.join()
print("Hi there!")
