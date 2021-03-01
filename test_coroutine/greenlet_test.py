from greenlet import greenlet
import time


def func1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)


def func2():
    while True:
        print('---B---')
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()
