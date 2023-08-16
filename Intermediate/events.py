import threading

event = threading.Event()


def function():
    print('Waiting for event to trigger...')
    event.wait()
    print('Performing action...')


t1 = threading.Thread(target=function)
t1.start()

x = input('Do you want to trigger the event? [Y/N]\n')
if x == 'y':
    event.set()
