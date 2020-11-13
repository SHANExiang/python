from threading import Lock


class ShareCounter():
    def __init__(self, init_num):
        self._init_num = init_num
        self._lock = Lock()

    def incr(self, delta=1):
        with self._lock:
            self._init_num += delta

    def decr(self, delta):
        with self._lock:
            self._init_num -= delta


# Lock 对象和 with 语句块一起使用可以保证互斥执行，就是每次只有一个线程可以
# 执行 with 语句包含的代码块。with 语句会在这个代码块执行前自动获取锁，在执行结
# 束后自动释放锁。
