'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
# xiaoxiaole, per each char in the string, check if the previous char in the stack can be paired with it, if yes, pop
# if it is valid parenthesis pairs, stack should be empty at the end 
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                last = stack[-1]
                if c == ')' and last == '(':
                    stack.pop()
                elif c == ']' and last == '[':
                    stack.pop()
                elif c == '}' and last == '{':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0
