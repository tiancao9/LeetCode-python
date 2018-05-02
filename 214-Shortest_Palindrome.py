'''
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"

'''
# find longest palindrome centered to the left part and pad the ramaining to the front
# t = s + "#" + s[::-1]
# KMP, Next[i] is the longest prefix==poxfix for t[:i+1]
class Solution:
    
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return s
        
        t = s + "#" + s[::-1] # add '#' for case: s = 'aabba': t = aabbaabbaa
        i = 1
        
        Next = [0]*len(t)
        
        while i < len(t):
            k = Next[i-1]
            while k > 0 and t[i] != t[k]:
                k = Next[k-1]
            if t[i] == t[k]: 
                Next[i] = k + 1
            else: 
                Next[i] = 0
            i += 1
        
        k = Next[-1]
        pad = s[k:][::-1]
        return pad+s

