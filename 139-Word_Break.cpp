'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

# DP, DP[i] == True means wordbreak(s[:i+1]) == True
# DP[i] == True if DP[j] == True and s[j+1:i+1] in wordDict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in range(len(s)):
            #if s[:i+1] itself is in wordDict
            if s[:i+1] in wordDict:
                dp[i] = True
            for j in range(i):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = True
        return dp[len(s)-1]


