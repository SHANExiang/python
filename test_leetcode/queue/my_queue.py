

# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
#
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
#
# 说明：
#
# 你只能使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#

class MyQueue:

    def __init__(self):
        self.in_list = []
        self.out_list = []

    def push(self, x: int) -> None:
        self.in_list.append(x)

    def pop(self) -> int:
        if self.out_list:
            return self.out_list.pop()
        else:
            for _ in range(len(self.in_list)):
                self.out_list.append(self.in_list.pop())
            return self.out_list.pop()

    def peek(self) -> int:
        if self.out_list:
            return self.out_list[-1]
        else:
            return self.in_list[0]

    def empty(self) -> bool:
        if not self.out_list and not self.in_list:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
