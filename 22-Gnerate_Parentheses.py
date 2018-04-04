'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
# add '(' when left < n, add ')' when right < left < n, append cur when left == n and right == n
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur = ""
        self.dfs(0, 0, cur, res, n)
        return res
        
    def dfs(self, left, right, cur, res, n):
        if left == n and right == n:
            res.append(cur)
            return
        if left < n:
            cur = cur + '('
            self.dfs(left+1, right, cur, res, n)
            cur = cur[:-1]
        if right < n and right < left:
            cur = cur + ')'
            self.dfs(left, right+1, cur, res, n)
            cur = cur[:-1]
