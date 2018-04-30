'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''
# USe list to record start point (+1) and end point (-1)
# count++ if item[1] == 1, else count--, max_r = max(max_r, count)


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        timing = []
        for i in range(len(intervals)):
            timing.append([intervals[i].start, 1])
            timing.append([intervals[i].end, -1])
        timing.sort()
        max_r = 0
        room = 0
        for item in timing:
            if item[1] == 1:
                room += 1
                max_r = max(max_r, room)
            else:
                room -= 1
        return max_r

