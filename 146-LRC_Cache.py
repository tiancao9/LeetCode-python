'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
# Double linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_dict = {}
        
    def add(self, node):
        """
        :type key: node
        :rtype: void
        """
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        self.key_dict[node.key] = node
        
    def remove(self,node):
        """
        :type key: int
        :rtype: void
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_dict[node.key]

        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_dict:
            node = self.key_dict[key]
            self.remove(node)
            self.add(node)
            return self.key_dict[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_dict:
            self.remove(self.key_dict[key])
            node = Node(key, value)
            self.add(node)
        else:
            if len(self.key_dict) >= self.capa:
                n = self.head.next
                self.remove(n)
            node = Node(key, value)
            self.add(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
