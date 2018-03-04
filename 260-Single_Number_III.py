'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

'''
# Time: O(n) Space: O(1)
# Iteration 1st: find the xor for the 2 different number and get the 1st 1 by diff &= -diff (-diff = complement of (diff-1))
# Iteration 2nd: compare each num with diff (the single 1), seperate nums into 2 group, with the diff bit and without, then find the 2 number
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        res = [0, 0]
        for num in nums:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
