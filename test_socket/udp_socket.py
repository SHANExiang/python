import socketserver
import time


"""
UDP 服务器也可以通过使用 socketserver 库很容易的被创建。
"""


class TimeHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == "__main__":
    server = socketserver.UDPServer(('', 20000), TimeHandler)
    server.serve_forever()
