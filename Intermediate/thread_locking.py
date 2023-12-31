import threading
import time

# thread locking
x = 8192

lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached Maximum")
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print('Reached the minimum')
    lock.release()


t1 = threading.Thread(target=double())
t2 = threading.Thread(target=halve())
t1.start()
t2.start()