'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''
# TrieNode: bool is_word and trienode_list
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.trienode_list = [None]*26
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if not cur.trienode_list[ord(c)-ord('a')]:
                cur.trienode_list[ord(c)-ord('a')] = TrieNode()
            cur = cur.trienode_list[ord(c)-ord('a')]
        cur.is_word = True    
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if not cur.trienode_list[ord(c)-ord('a')]:
                return False
            cur = cur.trienode_list[ord(c)-ord('a')]
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if not cur.trienode_list[ord(c)-ord('a')]:
                return False
            cur = cur.trienode_list[ord(c)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
