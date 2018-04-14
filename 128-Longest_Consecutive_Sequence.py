'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

'''
# use set, find use while loop cur++ and cur--
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            l = 1
            cur = num
            while cur+1 in nums:
                l += 1
                cur += 1
                nums.remove(cur)
            cur = num
            while cur-1 in nums:
                l += 1
                cur -= 1
                nums.remove(cur)
            res = max(res,l)
        return res

