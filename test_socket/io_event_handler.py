import select
import socket
import time


class EventHandler(object):
    def fileno(self):
        raise NotImplemented('mush implement')

    def want_to_receive(self):
        return False

    def handler_receive(self):
        pass

    def want_to_send(self):
        return False

    def handler_send(self):
        pass


class UDPServer(EventHandler):
    def __init__(self, address):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(address)

    def fileno(self):
        return self.socket.fileno()

    def want_to_receive(self):
        return True


class UDPTimeServer(UDPServer):
    def handler_receive(self):
        msg, address = self.socket.recvfrom(1)
        self.socket.sendto(time.ctime().encode('ascii'), address)


class UDPEchoServer(UDPServer):
    def handler_receive(self):
        msg, address = self.socket.recvfrom(8192)
        self.socket.sendto(msg, address)


def event_loop(handlers):
    while True:
        want_receive = [h for h in handlers if h.want_to_receive()]
        want_send = [h for h in handlers if h.want_to_send()]
        can_recv, can_send, _ = select.select(want_receive, want_send, [])
        for h in can_recv:
            h.handler_receive()
        for h in can_send:
            h.handler_send()


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.socket.bind(address)
        self.socket.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.socket.fileno()

    def want_to_receive(self):
        return True

    def handler_receive(self):
        client, address = self.socket.accept()
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClient(EventHandler):
    def __init__(self, socket, handler_list):
        self.socket = socket
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.socket.fileno()

    def close(self):
        self.socket.close()
        self.handler_list.remove(self)

    def want_to_send(self):
        return True if self.outgoing else False

    def handler_send(self):
        nsent = self.socket.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):
    def want_to_receive(self):
        return True

    def handler_receive(self):
        data = self.socket.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


if __name__ == '__main__':
    # UDP服务器
    # handlers = [UDPEchoServer(('', 10000)), UDPTimeServer(('', 20000))]
    # event_loop(handlers)

    # 测试结果
    # >>> from socket import socket, AF_INET, SOCK_DGRAM
    # >>> s = socket(AF_INET, SOCK_DGRAM)
    # >>> s.sendto(b'', ('localhost', 20000))
    # 0
    # >>> s.recvfrom(128)
    # (b'Sun Dec  6 22:06:34 2020', ('127.0.0.1', 20000))
    # >>> s.sendto(b'', ('localhost', 10000))
    # 0
    # >>> s.recvfrom(128)
    # (b'', ('127.0.0.1', 10000))


    # TCP 服务器
    handlers = []
    handlers.append(TCPServer(('', 10000), TCPEchoClient, handlers))
