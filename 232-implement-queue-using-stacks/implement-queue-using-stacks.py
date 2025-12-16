class MyQueue(object):

    def __init__(self):
        self.data = []
        self.front = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        val = self.data[self.front]
        self.front += 1
        return val

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        return self.data[self.front]

    def empty(self):
        """
        :rtype: bool
        """
        return self.front == len(self.data)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()