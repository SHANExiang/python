import socket
import threading
from concurrent.futures import ThreadPoolExecutor


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
        # t = threading.Thread(target=communicate, args=(conn, ))
        # t.start()
        pool.submit(communicate, conn)


if __name__ == '__main__':
    # 最多可开client端为2个
    pool = ThreadPoolExecutor(2)
    server('127.0.0.1', 8000)

