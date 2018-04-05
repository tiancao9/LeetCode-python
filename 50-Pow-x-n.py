'''
Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
'''

# convert n to binary, either use bit operation n & 1 << i or bin(n)[2:][i]
# iterate from 0 to 31
# for each iteration, x *= x, res *= x if bin[i] == 1
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        """
        flag = 1
        if n < 0:
            flag = -1
            n = n * -1
        m = bin(n)[2:] # m is a string
        res = 1
        p = x
        while m:
            if m[-1] == '1':
                res *= p
            p *= p
            m = m[:-1]
        if flag == -1:
            res = 1.0 / res
        return res
        """
        
        flag = True
        if n < 0:
            flag = False
            n = n * -1
        res = 1
        for i in range (32):
            if n & 1 << i:
                res *= x;
            x *= x
        if not flag:
            res = 1.0 / res
        return res
