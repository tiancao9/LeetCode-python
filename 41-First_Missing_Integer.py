Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while(i < len(nums)):
            if(nums[i] > 0 and (nums[i] != i+1) and (nums[i]-1 < len(nums))):
                a,b = i, nums[i]-1
                nums[a], nums[b] = nums[b], nums[a]
                if(nums[a] != nums[b]):
                    i -= 1
            i += 1 
        for i in range(len(nums)):
            if(nums[i] != i+1):
                return i+1
        return len(nums)+1
