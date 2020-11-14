from collections import defaultdict


class Exchange(object):
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task(object):
    def send(self):
        pass


task1 = Task()
task2 = Task()

exc = get_exchange('name')


exc.attach(task1)
exc.attach(task2)


exc.send('dong')
exc.send('xiang')

exc.detach(task1)
exc.detach(task2)