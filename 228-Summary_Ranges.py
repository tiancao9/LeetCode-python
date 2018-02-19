'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            left = i
            while i < len(nums)-1 and nums[i+1] == nums[i]+1:
                i += 1
            cur = str(nums[left])
            if(i > left):
                cur += "->" #string use += instead of append(), list use append()
                cur += str(nums[i])
            res.append(cur)
            i += 1 # no i++ for for-loop in python
        return res
