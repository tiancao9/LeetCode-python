'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Time: O(knlogk)

Sol1: Queue.PriorityQueue, pq.put(), pq.get()
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        dummy = ListNode(0)
        cur = dummy
        for l in lists:
            if l: q.put((l.val,l))
        while not q.empty():
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next     


Sol2:heapq, heapq.heapify(q), heapq.heappush(), heapq.heappop()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Compiler error, need to define __lt__ in class ListNode
'''
def __lt__(self,other):
        return self.intAttribute < other.intAttribute
'''
class Solution:
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        dummy = ListNode(0)
        cur = dummy
        for l in lists:
            if l: q.append((l.val,l))
        heapq.heapify(q)
        while len(q) != 0:
            cur = heapq.heappop(q)[1]
            if cur.next:
                heapq.heappush(q, (cur.next.val, cur.next))
            cur = cur.next
        return dummy.next
