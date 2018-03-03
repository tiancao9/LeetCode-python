'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
#static DP
class Solution:
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self.dp

        while len(dp) <= n:
            dp.append(dp[-1] + 1)
            j = 1
            i = len(dp)-1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
                
        return dp[n]
