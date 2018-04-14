'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_char = {}
        for c in s:
            if c in dict_char:
                dict_char[c] += 1
            else:
                dict_char[c] = 1
        for i in range(len(s)):
            if dict_char[s[i]] == 1:
                return i
        return -1

