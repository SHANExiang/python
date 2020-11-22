import queue


"""
Write a Python program to create a queue and display all the members and 
size of the queue.
Expected Output:
Members of the queue:
0 1 2 3
Size of the queue:
4
"""


def create_queue():
    q = queue.Queue()
    for x in range(4):
        q.put(x)
    print('Members of the queue:')
    for x in list(q.queue):
        print(x, end=' ')
    print('\nSize of the queue:')
    print(q.qsize())
    print(list(q.queue))
    print(q.empty())
    while not q.empty():
        print(q.get(), end=' ')
    print('\n%s' % q.empty())

    q2 = queue.LifoQueue()
    for x in range(4):
        q2.put(x)
    print(list(q2.queue))
    while not q2.empty():
        print(q2.get(), end=' ')


create_queue()
# Members of the queue:
# 0 1 2 3
# Size of the queue:
# 4
# [0, 1, 2, 3]
# False
# 0 1 2 3
# True
# [0, 1, 2, 3]
# 3 2 1 0
