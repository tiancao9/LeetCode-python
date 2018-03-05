'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''
# Time:O(n*k^2) Space: O(n)
class Solution:
    def is_palindrome(self, word):
        return word == word[::-1]
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {word: i for i, word in enumerate(words)}
        res = []
        for i in range(len(words)):
            cur = words[i]
            j = 0
            while(j <= len(cur)):
                pref = cur[:j]
                sef = cur[j:]
                if j != len(cur) and pref[::-1] in lookup and self.is_palindrome(sef) and pref[::-1] != cur:
                    res.append([i, lookup[pref[::-1]]])
                if sef[::-1] in lookup and self.is_palindrome(pref) and sef[::-1] != cur:
                    res.append([lookup[sef[::-1]], i])
                j += 1
        return res;
