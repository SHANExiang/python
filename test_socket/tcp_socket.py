import socket
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler


class EchoHandler1(BaseRequestHandler):
    def handle(self) -> None:
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


class EchoHandler2(StreamRequestHandler):
    def handler(self):
        print('Got connection from', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)


def echo_handler(address, client_socket):
    print('Got connection from', address)
    while True:
        msg = client_socket.recv(8192)
        if not msg:
            break
        client_socket.send(msg)


def echo_server(address, backlog=5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_socket, client_addr = sock.accept()
        echo_handler(client_addr, client_socket)


if __name__ == "__main__":
    # server = TCPServer(('', 20000), EchoHandler1)
    # server.serve_forever()

    echo_server(('', 20000))
