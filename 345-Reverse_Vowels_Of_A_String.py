'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''
# 2 pointer will time exceed, since python can not swap 2 char directly, have to make a list and swap then cascade 
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ""
        for c in s:
            if c in 'aeiouAEIOU':
                vowels += c
        res = ""
        for c in s:
            if c in 'aeiouAEIOU':
                res += vowels[-1:]
                vowels = vowels[:-1]
            else:
                res += c
        return res
