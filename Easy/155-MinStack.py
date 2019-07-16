# My Answer
'''
Runtime: 852 ms, faster than 9.41% of Python online submissions for Min Stack.
Memory Usage: 15.5 MB, less than 88.48% of Python online submissions for Min Stack.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return min(self.stack)
    
# Solution
'''
Runtime: 52 ms, faster than 87.35% of Python online submissions for Min Stack.
Memory Usage: 15.8 MB, less than 45.87% of Python online submissions for Min Stack.

from https://leetcode.com/problems/min-stack/discuss/237368/Python-1-line
'''
class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x: int):
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        if len(self.data) > 1: self.data.pop()

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]