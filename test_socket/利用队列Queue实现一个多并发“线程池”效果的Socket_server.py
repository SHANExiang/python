from queue import Queue
import socket
from threading import Thread


class MyThread(object):
    def __int__(self, max_thread):
        self.max_thread = max_thread
        self.q = self.queue = Queue(max_thread)

    def put_thread(self):
        for i in range(self.max_thread):
            self.q.put(Thread)

    def get_thread(self):
        return self.q.get()


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print('Client Data:', data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError:
            break


def server(ip, post):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, post))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        thread1 = pool.get_thread()
        obj = thread1(target=communicate, args=(conn, ))
        obj.start()


if __name__ == '__main__':
    pool = MyThread(4)
    server('127.0.0.1', 8001)
