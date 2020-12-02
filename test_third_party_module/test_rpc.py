from multiprocessing.connection import Listener
import pickle
from threading import Thread
import traceback
from xmlrpc.server import SimpleXMLRPCServer


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('connection closed')


def echo_server(address, authkey):
    server = Listener(address, authkey=authkey)
    while True:
        try:
            client = server.accept()
            echo_client(client)
        except:
            traceback.print_exc()


# echo_server(('', 25000), authkey=b'peekaboo')
# 交互式解释器中测试
# >>> from multiprocessing.connection import Client
# >>> c = Client(('localhost', 25000), authkey=b'peekaboo')
# >>> c.send('hello')
# >>> c.recv()
# 'hello'
# >>> c.send(100)
# >>> c.recv()
# 100
# >>> c.send([1, 2, 3, 4])
# >>> c.recv()
# [1, 2, 3, 4]
# >>>


class KeyValueServer(object):
    _registry_functions = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._server = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._registry_functions:
            self._server.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def server_forever(self):
        self._server.serve_forever()

# 服务端开启
# key_value_serve = KeyValueServer(('', 25000))
# key_value_serve.server_forever()

# 交互式解释器测试
# >>> s.set('name', 'dongxiang')
# >>> s.get('name')
# 'dongxiang'
# >>> s.exists('name')
# True
# >>> s.keys()
# ['name']
# >>> s.delete('name')
# >>> s.get('name')


class RPCHandler(object):
    def __init__(self):
        self._functions = dict()

    def registry_function(self, func):
        self._functions[func.__name__]  = func

    def handler_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    result = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(result))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handler_connection, args=(client,))
        t.daemon = True
        t.start()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class RPCProxy(object):
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(Exception, result):
                raise result
            return result
        return do_rpc


rpc = RPCHandler()
rpc.registry_function(add)
rpc.registry_function(sub)


rpc_server(handler=rpc, address=('', 25000), authkey=b'peekaboo')

# 使用的话
# from multiprocessing.connection import Client
# c = Client(('localhost', 25000), authkey=b'peekaboo')
# rpc = RPCProxy(c)
# rpc.add(1, 2)
# rpc.sub(3, 2)
