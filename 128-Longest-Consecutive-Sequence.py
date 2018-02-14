'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = {x: False for x in nums}
        res = 0
        for num in nums:
            length = 0
            cur = num;
            if hashset[cur] == False:
                while cur in nums:
                    length += 1; hashset[cur] = True; cur += 1; 
                cur = num-1;
                while cur in nums:
                    length += 1; hashset[cur] = True; cur -= 1;
            res = max(res, length)
        return res
