class MinStack(object):

    def __init__(self):
        self.Stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        min_val = self.getMin() 
        if min_val == None or min_val > val:
            min_val = val 
        self.Stack.append([val, min_val]) 

    def pop(self):
        """
        :rtype: None
        """
        self.Stack.pop() 

    def top(self):
        """
        :rtype: int
        """
        return self.Stack[-1][0] if self.Stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.Stack[-1][1] if self.Stack else None 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()