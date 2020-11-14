from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        thread = Thread(target=self._bootstrap)
        thread.daemon = True
        thread.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print(msg)


# p = PrintActor()
# p.start()
# p.send('hello')
# p.send(ActorExit())
# p.send('world')
# p.close()
# p.join()

# ****************************************************************************


class ToggedActor(Actor):
    def run(self):
        while True:
            func, *args = self.recv()
            print(func, *args)
            getattr(self, func)(*args)

    def A_func(self, x):
        print('A_func get', x)

    def B_func(self, x, y, z):
        print('B_func get %s, %s, %s' % (x,  y, z))


# t = ToggedActor()
# t.start()
# t.send(('A_func', 10))
# t.send(('B_func', 1, 2, 3))
# t.close()
# t.join()

# ****************************************************************************


class Result(object):
    def __init__(self):
        self._event = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._event.set()

    def result(self):
        self._event.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


work = Worker()
work.start()
rr = work.submit(pow, 2, 3)
print(rr.result())


