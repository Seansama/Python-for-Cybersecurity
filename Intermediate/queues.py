# FiFo queue
import queue

q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for i in numbers:
    q.put(i)

while not q.empty():
    print(q.get())


# LiFo queue

q2 = queue.LifoQueue()

digits = [10, 20, 30, 40, 50, 60]
for i in digits:
    q2.put(i)

while not q2.empty():
    print(q2.get())


# Priority queue

q3 = queue.PriorityQueue()

q3.put((2, 'Hello world'))
q3.put((11, 99))
q3.put((34, 12))
q3.put((22, True))

while not q3.empty():
    print(q3.get())
