

class Connection(object):
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, new_state):
        self._state = new_state

    def read(self):
        self._state.read(self)

    def write(self, data):
        self._state.write(self, data)

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)


class ConnectionState():
    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

    @staticmethod
    def read(conn):
        raise RuntimeError('not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('not open')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')


if __name__ == '__main__':
    conn = Connection()
    conn.open()
    conn.read()
    conn.close()
    print(conn._state)
    conn.write('dong')
