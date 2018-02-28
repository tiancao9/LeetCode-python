'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
# time: O(n) space: O(1) -> up to 26 letters
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lookup = {}
        for i in range(len(magazine)):
            if magazine[i] in lookup.keys():
                lookup[magazine[i]] += 1
            else:
                lookup[magazine[i]] = 1
        for i in range(len(ransomNote)):
            if ransomNote[i] in lookup.keys() and lookup[ransomNote[i]] > 0:
                lookup[ransomNote[i]] -= 1
            else:
                return False
        return True
            
