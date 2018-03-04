'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''

# result kepp the last index for each c in s
# while iterate s, for each c, if it is not in result, compare it with last char in result, pop result if last char is larger than char and the last char will appear later 
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rindex = {c: i for i, c in enumerate(s)}
        result = ""
        for i, c in enumerate(s):
            if c in result:
                continue
            while c < result[-1:] and i < rindex[result[-1:]]:
                result = result[:-1]
            result += c
        return result
            
