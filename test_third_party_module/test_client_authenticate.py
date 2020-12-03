import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM


def client_authenticate(connection, secret_key):
    msg = connection.recv()
    hash = hmac.new(secret_key, msg, '')
    digest = hash.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    msg = os.urandom(32)
    connection.send(msg)
    hash = hmac.new(secret_key, msg, '')
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)


secret_key = b'peekaboo'


def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c)


echo_server(('', 25000))


# 客户端内测试：
# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 25000))
# client_authenticate(s, secret_key)
# s.send(b'hello')
# resp = s.recv(1024)
