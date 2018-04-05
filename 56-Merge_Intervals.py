'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Sort the list with start para, sorted(interval, key = lambda i: i.start)
# compare current item with res[-1], if cur.start < res[-1].end, res[-1].end = max(cur.end, res[-1].end), else res.append(cur)
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        d = sorted(intervals, key = lambda i: i.start)
        for i in range(len(d)):
            cur = d[i]
            if i != 0 and cur.start <= res[-1].end:
                res[-1].end = max(cur.end, res[-1].end)
            else:
                res.append(cur)
            
        return res
            

