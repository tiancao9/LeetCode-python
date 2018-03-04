'''
Given an integer, write a function to determine if it is a power of two.
'''
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1 and n %2 == 0:
            n /= 2
        if n == 1:
            return True
        else:
            return False
