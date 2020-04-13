"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.__stack:
            self.__stack.append((x, x))
        else:
            self.__stack.append((x, min(x, self.__stack[-1][1])))

    def pop(self):
        """
        :rtype: None
        """
        if self.__stack:
            self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.__stack[-1][0] if self.__stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.__stack[-1][1] if self.__stack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
