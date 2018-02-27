'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        s = s.split(" ")
        for word in s:
            res += word[::-1] #reverse a string
            res += " "
        return res[:-1] #remove last " "
