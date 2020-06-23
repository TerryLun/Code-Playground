"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


def isValid(s):
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    stack = []
    for b in s:
        if b == '(' or b == '{' or b == '[':
            stack.append(b)
        elif not stack:
            return False
        elif b == ')' and stack[-1] == '(':
            stack.pop()
        elif b == '}' and stack[-1] == '{':
            stack.pop()
        elif b == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    if not stack:
        return True
    return False


Input = "()"
Output = True
actual = isValid(Input)
print(Output, actual)

Input = "()[]{}"
Output = True
actual = isValid(Input)
print(Output, actual)

Input = "(]"
Output = False
actual = isValid(Input)
print(Output, actual)

Input = "){"
Output = False
actual = isValid(Input)
print(Output, actual)

Input = "{[]}"
Output = True
actual = isValid(Input)
print(Output, actual)

