class MinStack(object):

    def __init__(self):
        self.stack_ans=list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack_ans.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack_ans.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack_ans[-1]

    def getMin(self):
        """
        :rtype: int
        """
        min=self.stack_ans[0]
        for x in self.stack_ans:
            if min > x:
                min = x
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()